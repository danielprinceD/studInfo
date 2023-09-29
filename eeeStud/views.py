
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
