from django import forms
from django.db import models
from django import forms  
from .models import cseStud,cseStud2,cseStud3,cseStud4

class Year1Form(forms.ModelForm):
    
    class Meta:
        model=cseStud
        fields='__all__'

class Year2Form(forms.ModelForm):
    
    class Meta:
        model=cseStud2
        fields='__all__'
