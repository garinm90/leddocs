from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect, render
from django.core import serializers

from rest_framework import viewsets

from .serializers import JobSerializer
from .models import Job, Customer, Ride, Light, LightCount, Image
from .forms import CustomerRideForm, JobForm, ImageForm


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class IndexView(RedirectView):
    url = reverse_lazy("list_jobs")


class JobDetailView(DetailView):
    model = Job
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_pk = self.kwargs.get(self.pk_url_kwarg)
        context["lights"] = LightCount.objects.filter(job__pk=job_pk)
        return context


class JobListView(ListView):
    model = Job
    context_object_name = "job_list"


class JobCreateView(CreateView):
    model = Job
    form_class = JobForm


class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm


class RideDetailView(DetailView):
    model = Ride


class RideCreateView(CreateView):
    model = Ride
    fields = "__all__"


class RideUpdateView(UpdateView):
    model = Ride
    fields = "__all__"


class RideListView(ListView):
    model = Ride
    context_object_name = "ride_list"


class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = "customer"


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = "__all__"

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        if hasattr(self, "object"):
            kwargs.update({"instance": self.object})
        return kwargs


class CustomerCreateView(CreateView):
    model = Customer
    fields = "__all__"


class CustomerListView(ListView):
    model = Customer
    context_object_name = "customer_list"


class LightDetailView(DetailView):
    model = Light


class LightCreateView(CreateView):
    model = Light
    fields = "__all__"


class LightUpdateView(UpdateView):
    model = Light


class LightListView(ListView):
    model = Light


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm


def add_customer_rides(request, pk):
    customer = Customer.objects.get(pk=pk)
    form = CustomerRideForm()
    if request.method == "POST":
        form = CustomerRideForm(request.POST)
        rides = form.data.getlist("rides")
        if len(rides) > 0:
            for ride in rides:
                ride = Ride.objects.get(pk=int(ride))
                customer.rides.add(ride)
            return redirect(customer)

    rides = serializers.serialize("json", Ride.objects.all())
    return render(
        request, "jobs/customer_ride_form.html", {"form": form, "rides": rides}
    )
