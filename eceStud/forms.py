from django import forms
from django.db import models
from django import forms  
from .models import eceStud,eceStud2,eceStud3,eceStud4

class Year1Form(forms.ModelForm):
    
    class Meta:
        model=eceStud
        fields='__all__'

class Year2Form(forms.ModelForm):
    
    class Meta:
        model=eceStud2
        fields='__all__'

class Year3Form(forms.ModelForm):
    
    class Meta:
        model=eceStud3
        fields='__all__'

class Year4Form(forms.ModelForm):
    
    class Meta:
        model=eceStud4
        fields='__all__'