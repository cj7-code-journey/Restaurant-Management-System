from django import forms
from icode_app.models import *

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"
        
class reservationform(forms.ModelForm):
    class Meta:
        model=reservation
        fields="__all__"
        