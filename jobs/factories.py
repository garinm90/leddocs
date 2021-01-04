import factory
import random

from .models import Customer, Light, LightCount, Ride, Job


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
        django_get_or_create = ("company",)

    company = factory.Faker("company")
    primary_contact = factory.Faker("name")
    primary_phone_number = factory.Faker("phone_number")
    email = factory.Faker("ascii_email")


class RideFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ride
        django_get_or_create = ("ride_name",)

    manufacturer = factory.Faker("company")
    ride_name = factory.Faker("first_name")


class LightFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Light
        # django_get_or_create = ("light_style",)

    lights = ["puck", "bubble", "long"]

    number_of_leds = factory.Faker("random_int", min=1, max=36)
    light_style = random.choice(lights)


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job

    job_date = factory.Faker("date_object")
    customer = factory.SubFactory(CustomerFactory)
    ride = factory.SubFactory(RideFactory)
    light = factory.SubFactory(LightFactory)


class LightCountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LightCount

    light = factory.SubFactory(LightFactory)
    job = factory.SubFactory(JobFactory)
    number_of_lights = factory.Faker("random_digit")


class JobWithLightFactory(factory.django.DjangoModelFactory):
    lights = factory.RelatedFactory(LightCountFactory, factory_related_name="lights")
