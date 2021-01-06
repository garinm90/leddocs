from django import forms
from .models import Job, Customer
from dal.autocomplete import ModelSelect2


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        widgets = {"customer": ModelSelect2(url="autocomplete_customer")}
