from django.shortcuts import render
from .models import cseStud

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
