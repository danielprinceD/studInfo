from unicodedata import name
from django.shortcuts import render,redirect
from .models import eeeStud
from .models import eeeStud2 ,eeeStud3,eeeStud4
from .forms import Year1Form
from .forms import Year2Form
from .forms import Year3Form
from .forms import Year4Form

# Create your views here.

def eee(request):
    return render(request,'eeeStud/year.html')
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

def profile2(request,id):
    profil=eeeStud2.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'eeeStud/profile2.html',context=pro)

def profile3(request,id):
    profil=eeeStud3.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'eeeStud/profile3.html',context=pro)

def profile4(request,id):
    profil=eeeStud4.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'eeeStud/profile4.html',context=pro)


# DELETE

def delete(request,id):
    delet=eeeStud.objects.get(id=id)
    delet.delete()
    return redirect('/eee/year1/')

def delete2(request,id):
    delet=eeeStud2.objects.get(id=id)
    delet.delete()
    return redirect('/eee/year2/')

def delete3(request,id):
    delet=eeeStud3.objects.get(id=id)
    delet.delete()
    return redirect('/eee/year3/')

def delete4(request,id):
    delet=eeeStud4.objects.get(id=id)
    delet.delete()
    return redirect('/eee/year4/')
    

# UPDATE


def update(request, id):
    form=Year1Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        eee_stud = eeeStud.objects.get(id=id)
    except eeeStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/eee/year1/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year1Form(request.POST, instance=eee_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/eee/year1/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year1Form(instance=eee_stud)
        
    return render(request, 'eeeStud/update.html', {'form': form, 'profile': eee_stud})
def update2(request, id):
    form=Year2Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        eee_stud = eeeStud2.objects.get(id=id)
    except eeeStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/eee/year2/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year2Form(request.POST, instance=eee_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/eee/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year2Form(instance=eee_stud)
        
    return render(request, 'eeeStud/update.html', {'form': form, 'profile': eee_stud})


def update3(request, id):
    form=Year3Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        eee_stud = eeeStud3.objects.get(id=id)
    except eeeStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/eee/year3/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year3Form(request.POST, instance=eee_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/eee/year3/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year3Form(instance=eee_stud)
        
    return render(request, 'eeeStud/update.html', {'form': form, 'profile': eee_stud})
def update4(request, id):
    form=Year4Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        eee_stud = eeeStud4.objects.get(id=id)
    except eeeStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/eee/year4/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year4Form(request.POST, instance=eee_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/eee/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year4Form(instance=eee_stud)
        
    return render(request, 'eeeStud/update.html', {'form': form, 'profile': eee_stud})



# SEARCH


# CREATE

def create1(request):
    form=Year1Form()
    if request.method=='POST':
        form=Year1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/eee/year1/')    
    return render(request,'eeeStud/create1.html',{'form':form})  

def create2(request):
    form=Year2Form()
    if request.method=='POST':
        form=Year2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/eee/year2/')    
    return render(request,'eeeStud/create2.html',{'form':form})  
def create3(request):
    form=Year3Form()
    if request.method=='POST':
        form=Year3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/eee/year3/')    
    return render(request,'eeeStud/create3.html',{'form':form})  
def create4(request):
    form=Year4Form()
    if request.method=='POST':
        form=Year4Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/eee/year4/')    
    return render(request,'eeeStud/create4.html',{'form':form})  