from django.db import models
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Job, Customer, Ride, Light, LightCount


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["job_list"] = Job.objects.all().order_by("last_updated_date")
        return context


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
