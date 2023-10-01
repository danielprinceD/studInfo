
# Create your views here.

# YEAR 
def year1(request):
    data=eeeStud.objects.all()
    sdata={'data':data}
    return render(request,'eeeStud/1year.html',context=sdata)

def year2(request):
    data=eeeStud2.objects.all()
    sdata={'data':data}
    return render(request,'eeeStud/2year.html',context=sdata)

def year3(request):
    data=eeeStud3.objects.all()
    sdata={'data':data}
    return render(request,'eeeStud/3year.html',context=sdata)

def year4(request):
    data=eeeStud4.objects.all()
    sdata={'data':data}
    return render(request,'eeeStud/4year.html',context=sdata)

# PROFILE


def profile(request,id):
    profil=eeeStud.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'eeeStud/profile.html',context=pro)
