from rest_framework import serializers
from .models import Job, Customer, Ride, Light, Image, LightCount


class JobSerializer(serializers.ModelSerializer):
    light = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"
        depth = 1

    def get_light(self, obj):
        qset = LightCount.objects.filter(job=obj)
        return [LightCountSerializer(m).data for m in qset]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = "__all__"


class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class LightCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightCount
        fields = (
            "number_of_lights",
            "job",
        )
