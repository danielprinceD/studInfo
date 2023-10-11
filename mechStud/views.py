from unicodedata import name
from django.shortcuts import render,redirect
from .models import mechStud
from .models import mechStud2 ,mechStud3,mechStud4
from .forms import Year1Form
from .forms import Year2Form
from .forms import Year3Form
from .forms import Year4Form

# Create your views here.

def mech(request):
    return render(request,'mechStud/year.html')
# YEAR 
def year1(request):
    data=mechStud.objects.all()
    sdata={'data':data}
    return render(request,'mechStud/1year.html',context=sdata)

def year2(request):
    data=mechStud2.objects.all()
    sdata={'data':data}
    return render(request,'mechStud/2year.html',context=sdata)

def year3(request):
    data=mechStud3.objects.all()
    sdata={'data':data}
    return render(request,'mechStud/3year.html',context=sdata)

def year4(request):
    data=mechStud4.objects.all()
    sdata={'data':data}
    return render(request,'mechStud/4year.html',context=sdata)

# PROFILE


def profile(request,id):
    profil=mechStud.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'mechStud/profile.html',context=pro)

def profile2(request,id):
    profil=mechStud2.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'mechStud/profile2.html',context=pro)

def profile3(request,id):
    profil=mechStud3.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'mechStud/profile3.html',context=pro)

def profile4(request,id):
    profil=mechStud4.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'mechStud/profile4.html',context=pro)


# DELETE

def delete(request,id):
    delet=mechStud.objects.get(id=id)
    delet.delete()
    return redirect('/mech/year1/')

def delete2(request,id):
    delet=mechStud2.objects.get(id=id)
    delet.delete()
    return redirect('/mech/year2/')

def delete3(request,id):
    delet=mechStud3.objects.get(id=id)
    delet.delete()
    return redirect('/mech/year3/')

def delete4(request,id):
    delet=mechStud4.objects.get(id=id)
    delet.delete()
    return redirect('/mech/year4/')
    

# UPDATE


def update(request, id):
    form=Year1Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        mech_stud = mechStud.objects.get(id=id)
    except mechStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/mech/year1/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year1Form(request.POST, instance=mech_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/mech/year1/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year1Form(instance=mech_stud)
        
    return render(request, 'mechStud/update.html', {'form': form, 'profile': mech_stud})
def update2(request, id):
    form=Year2Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        mech_stud = mechStud2.objects.get(id=id)
    except mechStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/mech/year2/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year2Form(request.POST, instance=mech_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/mech/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year2Form(instance=mech_stud)
        
    return render(request, 'mechStud/update.html', {'form': form, 'profile': mech_stud})


def update3(request, id):
    form=Year3Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        mech_stud = mechStud3.objects.get(id=id)
    except mechStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/mech/year3/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year3Form(request.POST, instance=mech_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/mech/year3/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year3Form(instance=mech_stud)
        
    return render(request, 'mechStud/update.html', {'form': form, 'profile': mech_stud})
def update4(request, id):
    form=Year4Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        mech_stud = mechStud4.objects.get(id=id)
    except mechStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/mech/year4/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year4Form(request.POST, instance=mech_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/mech/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year4Form(instance=mech_stud)
        
    return render(request, 'mechStud/update.html', {'form': form, 'profile': mech_stud})



# SEARCH


# CREATE

def create1(request):
    form=Year1Form()
    if request.method=='POST':
        form=Year1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mech/year1/')    
    return render(request,'mechStud/create1.html',{'form':form})  

def create2(request):
    form=Year2Form()
    if request.method=='POST':
        form=Year2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mech/year2/')    
    return render(request,'mechStud/create2.html',{'form':form})  
def create3(request):
    form=Year3Form()
    if request.method=='POST':
        form=Year3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mech/year3/')    
    return render(request,'mechStud/create3.html',{'form':form})  
def create4(request):
    form=Year4Form()
    if request.method=='POST':
        form=Year4Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mech/year4/')    
    return render(request,'mechStud/create4.html',{'form':form})  