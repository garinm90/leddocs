from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from dal.autocomplete import Select2QuerySetView
from rest_framework import viewsets

from .serializers import (
    JobSerializer,
    RideSerializer,
    CustomerSerializer,
    LightSerializer,
    ImageSerializer,
)
from .models import Job, Customer, Ride, Light, LightCount, Image
from .forms import JobForm, ImageForm


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
    # fields = "__all__"
    form_class = JobForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['formset'] = JobImageFormSet()
    #     return context

    # def post(self, request, *args, **kwargs):
    #     formset = JobImageFormSet(request.POST)
    #     form = self.get_form(JobForm)
    #     if formset.is_valid() and form.is_valid():
    #         return self.form_valid(formset,form)

    # def form_valid(self, form, formset,):
    #     object = form.save()
    #     formset.instance = self.object
    #     formset.save()
    #     return HttpResponseRedirect('/jobs/')


class JobUpdateView(UpdateView):
    model = Job
    # fields = "__all__"
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


class CustomerAutoComplete(Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Customer.objects.none()
        qs = Customer.objects.all()
        if self.q:
            qs = qs.filter(primary_contact__icontains=self.q)
        return qs


class JobAutoComplete(Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Job.objects.none()
        qs = Job.objects.all()
        if self.q:
            qs = qs.filter(customer__icontains=self.q)
        return qs


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm
