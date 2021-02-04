import debug_toolbar
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from jobs.urls import router as job_router

router = routers.DefaultRouter()
router.registry.extend(job_router.registry)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("grappelli/", include("grappelli.urls")),
    path("", include("jobs.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    path("api/v1/", include(router.urls)),
]
