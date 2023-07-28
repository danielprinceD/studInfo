from django.db import models
from django.forms import ModelForm 
from .models import cseStud

class Year1Form(ModelForm):
    class Meta:
        model=cseStud
        fields='__all__'