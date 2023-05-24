from unicodedata import name
from django.shortcuts import render,redirect
from .models import cseStud
from .models import cseStud2 ,cseStud3,cseStud4
from .forms import Year1Form
from .forms import Year2Form
from .forms import Year3Form
from .forms import Year4Form

# Create your views here.

def cse(request):
    return render(request,'cseStud/year.html')
