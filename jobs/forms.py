from django import forms
from django.forms import inlineformset_factory

# from dal.autocomplete import ModelSelect2
from .models import Customer, Job, Image, Ride

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomerRideForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ("company", "primary_contact", "email", "primary_phone_number")

    rides = forms.ChoiceField(
        widget=forms.SelectMultiple,
        choices=[(choice.pk, choice) for choice in Ride.objects.all()],
    )


# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = "__all__"
#         widgets = {
#             "customer": ModelSelect2(
#                 url="autocomplete_customer",
#                 attrs={
#                     "data-html": True,
#                 },
#             ),
#             "light": forms.widgets.CheckboxSelectMultiple(),
#         }


class JobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "job_form"
        self.helper.form_method = "post"
        self.helper.form_action = "create_job"
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta:
        model = Job
        fields = "__all__"

    # customer = forms.ChoiceField(
    #     choices=[(choice.pk, choice) for choice in Customer.objects.all()]
    # )


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


JobImageFormSet = inlineformset_factory(Job, Image, JobForm)