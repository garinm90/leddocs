from django.db import models
from django.urls import reverse

# from django.db.models.base import Model
# from django.db.models.deletion import CASCADE
# from django.db.models.fields import NullBooleanField


class Job(models.Model):
    customer = models.ForeignKey(
        "Customer", on_delete=models.SET_NULL, null=True, related_name="jobs"
    )
    ride = models.ForeignKey("Ride", on_delete=models.SET_NULL, null=True)
    job_date = models.DateField()
    job_start_date = models.DateField(auto_now_add=True)
    job_end_date = models.DateField(blank=True, null=True)
    last_updated_date = models.DateField(auto_now=True)
    light = models.ManyToManyField("Light", related_name="jobs", through="LightCount")

    def get_absolute_url(self):
        return reverse("detail_job", args=[str(self.id)])

    def __str__(self) -> str:
        return f"{self.customer.primary_contact}'s on {self.ride} start date: {self.job_start_date:%m-%d-%Y}"


class Customer(models.Model):
    company = models.CharField(max_length=50)
    primary_contact = models.CharField(max_length=50)
    primary_phone_number = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    def __str__(self) -> str:
        return self.primary_contact

    def get_absolute_url(self):
        return reverse("detail_customer", args=[str(self.id)])


class Ride(models.Model):
    ride_name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    alternate_name = models.CharField(max_length=50, blank=True)
    customers = models.ManyToManyField("Customer", related_name="rides")

    def __str__(self) -> str:
        return self.ride_name

    def get_absolute_url(self):
        return reverse("detail_ride", args=[str(self.id)])


class Light(models.Model):
    light_style = models.CharField(max_length=50)
    number_of_leds = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.light_style} {self.number_of_leds}"

    def get_absolute_url(self):
        return reverse("detail_light", args=[str(self.id)])


class LightCount(models.Model):
    number_of_lights = models.PositiveIntegerField()
    light = models.ForeignKey(Light, on_delete=models.SET_NULL, null=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.number_of_lights} {self.light}"
