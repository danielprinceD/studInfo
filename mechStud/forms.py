from django import forms
from django.db import models
from django import forms  
from .models import mechStud,mechStud2,mechStud3,mechStud4

class Year1Form(forms.ModelForm):
    
    class Meta:
        model=mechStud
        fields='__all__'

class Year2Form(forms.ModelForm):
    
    class Meta:
        model=mechStud2
        fields='__all__'

class Year3Form(forms.ModelForm):
    
    class Meta:
        model=mechStud3
        fields='__all__'

class Year4Form(forms.ModelForm):
    
    class Meta:
        model=mechStud4
        fields='__all__'