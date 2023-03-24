from django import forms
from django.db import models
from django import forms  
from .models import civilStud,civilStud2,civilStud3,civilStud4

class Year1Form(forms.ModelForm):
    
    class Meta:
        model=civilStud
        fields='__all__'
