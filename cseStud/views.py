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

def year3(request):
    data=cseStud3.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/3year.html',context=sdata)

def year4(request):
    data=cseStud4.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/4year.html',context=sdata)

# PROFILE


def profile(request,id):
    profil=cseStud.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile.html',context=pro)

def profile2(request,id):
    profil=cseStud2.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile2.html',context=pro)

def profile3(request,id):
    profil=cseStud3.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile3.html',context=pro)

def profile4(request,id):
    profil=cseStud4.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile4.html',context=pro)


# DELETE

def delete(request,id):
    delet=cseStud.objects.get(id=id)
    delet.delete()
    return redirect('/cse/year1/')

def delete2(request,id):
    delet=cseStud2.objects.get(id=id)
    delet.delete()
    return redirect('/cse/year2/')
