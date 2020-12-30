from django.contrib import admin
from django.urls import path
from users.views import Home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view())
    # path("user/", include("users.urls", namespace="user")),
]
