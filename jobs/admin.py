from django.contrib import admin
from .models import Ride, Light, Job, Customer, LightCount


class LightCountInline(admin.TabularInline):
    model = LightCount
    extra = 1


@admin.register(
    Light,
    Job,
)
class JobAdmin(admin.ModelAdmin):
    inlines = (LightCountInline,)


@admin.register(Ride, Customer)
class InfoAdmin(admin.ModelAdmin):
    pass
