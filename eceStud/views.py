from unicodedata import name
from django.shortcuts import render,redirect
from .models import eceStud
from .models import eceStud2 ,eceStud3,eceStud4
from .forms import Year1Form
from .forms import Year2Form
from .forms import Year3Form
from .forms import Year4Form

# Create your views here.

def ece(request):
    return render(request,'eceStud/year.html')
# YEAR 
def year1(request):
    data=eceStud.objects.all()
    sdata={'data':data}
    return render(request,'eceStud/1year.html',context=sdata)

def year2(request):
    data=eceStud2.objects.all()
    sdata={'data':data}
    return render(request,'eceStud/2year.html',context=sdata)
