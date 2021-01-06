from jobs.views import CustomerAutocomplete
from django import forms
from .models import Job, Customer


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        widgets = {
            "customer": forms.CheckboxSelectMultiple(choices=Customer.objects.all())
        }
