from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class Job(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.SET_NULL, null=True)
    ride = models.ForeignKey("Ride", on_delete=models.SET_NULL, null=True)
    job_date = models.DateField()
    job_start_date = models.DateField(auto_now_add=True)
    job_end_date = models.DateField()
    last_updated_date = models.DateField(auto_now=True)
    # number_of_lights = models.PositiveIntegerField()
    light = models.ManyToManyField("Light", related_name="lights", through="LightCount")

    def __str__(self) -> str:
        return f"Work done for {self.company} on {self.ride} job date: {self.job_date}"


class Customer(models.Model):
    company = models.CharField(max_length=50)
    primary_contact = models.CharField(max_length=50)
    primary_phone_number = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    def __str__(self) -> str:
        return self.primary_contact


class Ride(models.Model):
    ride_name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    alternate_name = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.ride_name


class Light(models.Model):
    light_style = models.CharField(max_length=50)
    number_of_leds = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.light_style} {self.number_of_leds}"


class LightCount(models.Model):
    number_of_lights = models.PositiveIntegerField()
    light = models.ForeignKey(Light, on_delete=models.SET_NULL, null=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)