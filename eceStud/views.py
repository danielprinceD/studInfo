from unicodedata import name
from django.shortcuts import render,redirect
from .models import eceStud
from .models import eceStud2 ,eceStud3,eceStud4
from .forms import Year1Form
from .forms import Year2Form
from .forms import Year3Form
from .forms import Year4Form

# Create your views here.

def ece(request):
    return render(request,'eceStud/year.html')
# YEAR 
def year1(request):
    data=eceStud.objects.all()
    sdata={'data':data}
    return render(request,'eceStud/1year.html',context=sdata)

def year2(request):
    data=eceStud2.objects.all()
    sdata={'data':data}
    return render(request,'eceStud/2year.html',context=sdata)

def year3(request):
    data=eceStud3.objects.all()
    sdata={'data':data}
    return render(request,'eceStud/3year.html',context=sdata)

def year4(request):
    data=eceStud4.objects.all()
    sdata={'data':data}
    return render(request,'eceStud/4year.html',context=sdata)

# PROFILE


def profile(request,id):
    profil=eceStud.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'eceStud/profile.html',context=pro)

def profile2(request,id):
    profil=eceStud2.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'eceStud/profile2.html',context=pro)

def profile3(request,id):
    profil=eceStud3.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'eceStud/profile3.html',context=pro)

def profile4(request,id):
    profil=eceStud4.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'eceStud/profile4.html',context=pro)


# DELETE

def delete(request,id):
    delet=eceStud.objects.get(id=id)
    delet.delete()
    return redirect('/ece/year1/')

def delete2(request,id):
    delet=eceStud2.objects.get(id=id)
    delet.delete()
    return redirect('/ece/year2/')

def delete3(request,id):
    delet=eceStud3.objects.get(id=id)
    delet.delete()
    return redirect('/ece/year3/')

def delete4(request,id):
    delet=eceStud4.objects.get(id=id)
    delet.delete()
    return redirect('/ece/year4/')
    

# UPDATE


def update(request, id):
    form=Year1Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        ece_stud = eceStud.objects.get(id=id)
    except eceStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/ece/year1/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year1Form(request.POST, instance=ece_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/ece/year1/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year1Form(instance=ece_stud)
        
    return render(request, 'eceStud/update.html', {'form': form, 'profile': ece_stud})
def update2(request, id):
    form=Year2Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        ece_stud = eceStud2.objects.get(id=id)
    except eceStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/ece/year2/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year2Form(request.POST, instance=ece_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/ece/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year2Form(instance=ece_stud)
        
    return render(request, 'eceStud/update.html', {'form': form, 'profile': ece_stud})


def update3(request, id):
    form=Year3Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        ece_stud = eceStud3.objects.get(id=id)
    except eceStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/ece/year3/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year3Form(request.POST, instance=ece_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/ece/year3/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year3Form(instance=ece_stud)
        
    return render(request, 'eceStud/update.html', {'form': form, 'profile': ece_stud})
def update4(request, id):
    form=Year4Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        ece_stud = eceStud4.objects.get(id=id)
    except eceStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/ece/year4/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year4Form(request.POST, instance=ece_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/ece/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year4Form(instance=ece_stud)
        
    return render(request, 'eceStud/update.html', {'form': form, 'profile': ece_stud})



# SEARCH


# CREATE

def create1(request):
    form=Year1Form()
    if request.method=='POST':
        form=Year1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ece/year1/')    
    return render(request,'eceStud/create1.html',{'form':form})  

def create2(request):
    form=Year2Form()
    if request.method=='POST':
        form=Year2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ece/year2/')    
    return render(request,'eceStud/create2.html',{'form':form})  
def create3(request):
    form=Year3Form()
    if request.method=='POST':
        form=Year3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ece/year3/')    
    return render(request,'eceStud/create3.html',{'form':form})  
def create4(request):
    form=Year4Form()
    if request.method=='POST':
        form=Year4Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ece/year4/')    
    return render(request,'eceStud/create4.html',{'form':form})  