from django import forms

from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        plen = len(phone_number)
        if plen != 0 and ( plen != 10 or not phone_number.isnumeric() ):
            raise forms.ValidationError('Phone number not valid')
        return phone_number
