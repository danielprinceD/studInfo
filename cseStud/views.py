from django.shortcuts import render

# Create your views here.

def cse(request):
    return render(request,'cseStud/base.html')
