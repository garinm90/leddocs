from django.urls import path
from .views import (
    IndexView,
    JobCreateView,
    JobDetailView,
    JobListView,
    RideCreateView,
    RideDetailView,
    RideListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDetailView,
    CustomerListView,
    LightCreateView,
    LightDetailView,
    LightListView,
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("job/<int:pk>", JobDetailView.as_view(), name="detail_job"),
    path("jobs", JobListView.as_view(), name="list_jobs"),
    path("job/new", JobCreateView.as_view(), name="create_job"),
    path("ride/<int:pk>", RideDetailView.as_view(), name="detail_ride"),
    path("rides", RideListView.as_view(), name="list_rides"),
    path("ride/new", RideCreateView.as_view(), name="create_ride"),
    path("customer/<int:pk>", CustomerDetailView.as_view(), name="detail_customer"),
    path(
        "customer/<int:pk>/update", CustomerUpdateView.as_view(), name="update_customer"
    ),
    path("customers", CustomerListView.as_view(), name="list_customers"),
    path("customer/new", CustomerCreateView.as_view(), name="create_customer"),
    path("light/<int:pk>", LightDetailView.as_view(), name="detail_light"),
    path("lights", LightListView.as_view(), name="list_lights"),
    path("light/new", LightCreateView.as_view(), name="create_light"),
]
