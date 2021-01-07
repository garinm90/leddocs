from django.urls import path

from .views import (
    IndexView,
    JobCreateView,
    JobDetailView,
    JobListView,
    JobUpdateView,
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
    CustomerAutoComplete,
    RideUpdateView,
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("job/<int:pk>", JobDetailView.as_view(), name="detail_job"),
    path("job/<int:pk>/update", JobUpdateView.as_view(), name="update_job"),
    path("jobs", JobListView.as_view(), name="list_jobs"),
    path("job/new", JobCreateView.as_view(), name="create_job"),
    path("ride/<int:pk>", RideDetailView.as_view(), name="detail_ride"),
    path("ride/<int:pk>/update", RideUpdateView.as_view(), name="update_ride"),
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
    path(
        "customer/autocomplete",
        CustomerAutoComplete.as_view(),
        name="autocomplete_customer",
    ),
]
