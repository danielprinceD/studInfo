from django import forms
from django.db import models
from django import forms  
from .models import civilStud,civilStud2,civilStud3,civilStud4

class Year1Form(forms.ModelForm):
    
    class Meta:
        model=civilStud
        fields='__all__'

class Year2Form(forms.ModelForm):
    
    class Meta:
        model=civilStud2
        fields='__all__'

class Year3Form(forms.ModelForm):
    
    class Meta:
        model=civilStud3
        fields='__all__'

class Year4Form(forms.ModelForm):
    
    class Meta:
        model=civilStud4
        fields='__all__'