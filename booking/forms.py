from django import forms
from .models import Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class BookingForm(forms.ModelForm):
    """
    Form for adding a booking item
    related to :model:`Booking`
    """
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
