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
# YEAR 
def year1(request):
    data=cseStud.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/1year.html',context=sdata)

def year2(request):
    data=cseStud2.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/2year.html',context=sdata)
