from django import forms
from django.db import models
from django.forms import ModelForm 
from .models import cseStud

class Year1Form(ModelForm):
    
    DOB=forms.DateField(widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}), required=True)
    class Meta:
        model=cseStud
        fields='__all__'