from django import forms

from dal.autocomplete import ModelSelect2
from .models import Job

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
