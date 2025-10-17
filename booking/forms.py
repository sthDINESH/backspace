from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from datetime import datetime, time

def business_hour_choices():
    # Generates choices from 08:00 to 22:00 in 30-minute increments
    choices = []
    for hour in range(8, 22 + 1):
        for minute in (0, 30):
            t = time(hour, minute)
            label = t.strftime('%H:%M')
            choices.append((label, label))
    return choices


class BookingForm(forms.ModelForm):
    """
    Form for adding a booking item
    related to :model:`Booking`
    """
    # Add dropdown fields that return strings like "08:30"
    start_time = forms.ChoiceField(
        choices=business_hour_choices(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    end_time = forms.ChoiceField(
        choices=business_hour_choices(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('workspace'),
            Field('booking_date'),
            Field('start_time'),
            Field('end_time'),
            Field('purpose'),
            Field('notes'),
        )

    class Meta:
        model = Booking
        fields = (
            'workspace',
            'booking_date',
            'start_time',
            'end_time',
            'purpose',
            'notes',
        )
        widgets = {
            'workspace': forms.HiddenInput(),
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    # Convert selected "HH:MM" strings into datetime.time objects for the model
    def clean_start_time(self):
        val = self.cleaned_data.get('start_time')
        try:
            return datetime.strptime(val, '%H:%M').time()
        except Exception:
            raise forms.ValidationError("Invalid start time format.")

    def clean_end_time(self):
        val = self.cleaned_data.get('end_time')
        try:
            return datetime.strptime(val, '%H:%M').time()
        except Exception:
            raise forms.ValidationError("Invalid end time format.")


class CheckBookingsForm(forms.Form):
    """
    Form to check existing reservations
    """
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    start_time = forms.ChoiceField(
        choices=business_hour_choices(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    end_time = forms.ChoiceField(
        choices=business_hour_choices(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('date'),
                Field('start_time'),
                Field('end_time'),
                css_class='d-flex gap-2 align-items-end'
            )
        )

