from django import forms
from django.db import models
from django import forms  
from .models import eeeStud,eeeStud2,eeeStud3,eeeStud4

class Year1Form(forms.ModelForm):
    
    class Meta:
        model=eeeStud
        fields='__all__'

class Year2Form(forms.ModelForm):
    
    class Meta:
        model=eeeStud2
        fields='__all__'

class Year3Form(forms.ModelForm):
    
    class Meta:
        model=eeeStud3
        fields='__all__'

class Year4Form(forms.ModelForm):
    
    class Meta:
        model=eeeStud4
        fields='__all__'