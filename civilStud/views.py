from unicodedata import name
from django.shortcuts import render,redirect
from .models import civilStud
# Create your views here.

def civil(request):
    return render(request,'civilStud/year.html')
# YEAR 

    return render(request,'civilStud/2year.html',context=sdata)



# PROFILE





def create3(request):
    form=Year3Form()
    if request.method=='POST':
        form=Year3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/civil/year3/')    
    return render(request,'civilStud/create3.html',{'form':form})  
def create4(request):
    form=Year4Form()
    if request.method=='POST':
        form=Year4Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/civil/year4/')    
    return render(request,'civilStud/create4.html',{'form':form})  