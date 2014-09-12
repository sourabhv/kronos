from django import forms

from .models import Applicant
from .workshops import WORKSHOPS_TEMPLATES


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        plen = len(phone_number)
        if plen != 0 and ( plen != 10 or not phone_number.isnumeric() ):
            raise forms.ValidationError('We won\'t prank call but please '
                                        'enter a valid phone number')
        return phone_number

    def clean_workshop(self):
        err_msg = 'Event not found. Did we screw up? Please report it to us then.'
        workshop = self.cleaned_data['workshop']
        if workshop not in WORKSHOPS_TEMPLATES:
            raise forms.ValidationError(err_msg)
        return workshop
