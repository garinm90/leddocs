from django import forms
from django.forms import inlineformset_factory
from dal.autocomplete import ModelSelect2
from .models import Job, Image

forms.Form


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        widgets = {
            "customer": ModelSelect2(
                url="autocomplete_customer",
                attrs={
                    "data-html": True,
                },
            ),
            "light": forms.widgets.CheckboxSelectMultiple(),
        }


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        widgets = {
            "customer": ModelSelect2(
                url="autocomplete_customer",
                attrs={
                    "data-html": True,
                },
            ),
            "light": forms.widgets.CheckboxSelectMultiple(),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
        widgets = {
            "job": ModelSelect2(
                url="autocomplete_job",
                attrs={
                    "data-html": True,
                },
            )
        }


JobImageFormSet = inlineformset_factory(Job, Image, JobForm)