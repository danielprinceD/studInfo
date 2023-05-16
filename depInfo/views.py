from django.shortcuts import render
from eceStud.models import eceStud
from eceStud.models import eceStud2 ,eceStud3,eceStud4

from cseStud.models import cseStud
from cseStud.models import cseStud2 ,cseStud3,cseStud4

from civilStud.models import civilStud
from civilStud.models import civilStud2 ,civilStud3,civilStud4

from eeeStud.models import eeeStud
from eeeStud.models import eeeStud2 ,eeeStud3,eeeStud4

from mechStud.models import mechStud
from mechStud.models import mechStud2 ,mechStud3,mechStud4
# Create your views here.
def depInfo(request):
 return render(request,'depInfo/depInfo.html')



def search(request):
    if request.method=='GET':
        search=request.GET.get('search')
        ece=eceStud.objects.all().filter(name=search)
        ece2=eceStud2.objects.all().filter(name=search)
        ece3=eceStud3.objects.all().filter(name=search)
        ece4=eceStud4.objects.all().filter(name=search)
        cse=cseStud.objects.all().filter(name=search)
        cse2=cseStud2.objects.all().filter(name=search)
        cse3=cseStud3.objects.all().filter(name=search)
        cse4=cseStud4.objects.all().filter(name=search)
        civil=civilStud.objects.all().filter(name=search)
        civil2=civilStud2.objects.all().filter(name=search)
 
