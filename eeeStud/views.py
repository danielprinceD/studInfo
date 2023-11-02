
# Create your views here.

# YEAR 
def year1(request):
    data=eeeStud.objects.all()
    sdata={'data':data}
    return render(request,'eeeStud/1year.html',context=sdata)
