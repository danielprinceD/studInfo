from django.shortcuts import render
from eceStud.models import eceStud
from eceStud.models import eceStud2 ,eceStud3,eceStud4

from cseStud.models import cseStud
from cseStud.models import cseStud2 ,cseStud3,cseStud4

from civilStud.models import civilStud
from civilStud.models import civilStud2 ,civilStud3,civilStud4

from eeeStud.models import eeeStud
from eeeStud.models import eeeStud2 ,eeeStud3,eeeStud4

# Create your views here.
def depInfo(request):
 return render(request,'depInfo/depInfo.html')



