from django.shortcuts import render,redirect
from .models import cseStud
from .forms import Year1Form

# Create your views here.

def cse(request):
    return render(request,'cseStud/year.html')

def year1(request):
    data=cseStud.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/1year.html',context=sdata)

def profile(request,id):
    profil=cseStud.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile.html',context=pro)

def delete(request,id):
    delet=cseStud.objects.get(id=id)
    delet.delete()
    return redirect('/depInfo/dep/cse/year1/')
    

def update(request,id):
    CseStud=cseStud.objects.get(id=id)
    if request.method=='POST':
        form=Year1Form(request.POST,instance=CseStud)
        if form.is_valid():
            form.save()
            return redirect('year1/')
    return render(request,'cseStud/update.html',{'profile':CseStud})



def create1(request):
    form=Year1Form()
    if request.method=='POST':
        form=Year1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/depInfo/dep/cse/year1/')    
    return render(request,'cseStud/create1.html',{'form':form})  