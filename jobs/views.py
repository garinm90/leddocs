from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from dal.autocomplete import Select2QuerySetView

from .models import Job, Customer, Ride, Light, LightCount
from .forms import JobForm


class IndexView(RedirectView):
    url = reverse_lazy("list_jobs")


class JobDetailView(DetailView):
    model = Job
    context_object_name = "job"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        job_pk = self.kwargs.get(self.pk_url_kwarg)
        context["lights"] = LightCount.objects.filter(job__pk=job_pk)
        return context


class JobListView(ListView):
    model = Job
    context_object_name = "job_list"


class JobCreateView(CreateView):
    model = Job
    fields = "__all__"
    # form_class = JobForm


class JobUpdateView(UpdateView):
    model = Job
    fields = "__all__"
    # form_class = JobForm


class RideDetailView(DetailView):
    model = Ride


class RideCreateView(CreateView):
    model = Ride
    fields = "__all__"


class RideUpdateView(UpdateView):
    model = Ride


class RideListView(ListView):
    model = Ride
    context_object_name = "ride_list"


class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = "customer"


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = "__all__"


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


class CustomerAutoComplete(Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Customer.objects.none()
        qs = Customer.objects.all()
        return qs
