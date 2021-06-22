from django import forms 
from django.forms import widgets 
from django.forms import fields
from app.models import * 


class DonorRegForm(forms.ModelForm):
    class Meta:
        model=DonorReg
        fields='__all__'  


class PatientRegForm(forms.ModelForm):
    class Meta:
        model=PatientReg 
        fields='__all__' 



class HospitalsForm(forms.ModelForm):
    class Meta:
        model=Hopitals
        fields='__all__'