from django.urls import path
from .views import IndexView, JobCreateView, JobDetailView, JobListView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("job/<int:id>", JobDetailView.as_view(), name="detail_job"),
    path("jobs", JobListView.as_view(), name="list_jobs"),
    path("job", JobCreateView.as_view(), name="create_job"),
]
