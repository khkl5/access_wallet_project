from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "guest",
            "room",
            "check_in",
            "check_out",
        ]
        widgets = {
            "check_in": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "check_out": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "guest": forms.Select(attrs={"class": "form-select"}),
            "room": forms.Select(attrs={"class": "form-select"}),
        }