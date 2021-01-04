from django.db import models
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Job, Customer, Ride, Light


class IndexView(TemplateView):
    template_name = "index.html"


class JobDetailView(DetailView):
    model = Job
    context_object_name = "job"


class JobListView(ListView):
    model = Job
    context_object_name = "job_list"


class JobCreateView(CreateView):
    model = Job
    fields = "__all__"
