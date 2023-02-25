from unicodedata import name
from django.shortcuts import render,redirect
from .models import civilStud
# Create your views here.

def civil(request):
    return render(request,'civilStud/year.html')
# YEAR 

    return render(request,'civilStud/2year.html',context=sdata)



# PROFILE






