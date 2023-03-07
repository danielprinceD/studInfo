from unicodedata import name
from django.shortcuts import render,redirect
from .models import civilStud
# Create your views here.

def civil(request):
    return render(request,'civilStud/year.html')
# YEAR 

    return render(request,'civilStud/2year.html',context=sdata)



# PROFILE

def delete3(request,id):
    delet=civilStud3.objects.get(id=id)
    delet.delete()
    return redirect('/civil/year3/')

def delete4(request,id):
    delet=civilStud4.objects.get(id=id)
    delet.delete()
    return redirect('/civil/year4/')
    

# UPDATE


def update(request, id):
    form=Year1Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        civil_stud = civilStud.objects.get(id=id)
    except civilStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/civil/year1/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year1Form(request.POST, instance=civil_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/civil/year1/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year1Form(instance=civil_stud)
        
    return render(request, 'civilStud/update.html', {'form': form, 'profile': civil_stud})
def update2(request, id):
    form=Year2Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        civil_stud = civilStud2.objects.get(id=id)
    except civilStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/civil/year2/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year2Form(request.POST, instance=civil_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/civil/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year2Form(instance=civil_stud)
        
    return render(request, 'civilStud/update.html', {'form': form, 'profile': civil_stud})


def update3(request, id):
    form=Year3Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        civil_stud = civilStud3.objects.get(id=id)
    except civilStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/civil/year3/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year3Form(request.POST, instance=civil_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/civil/year3/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year3Form(instance=civil_stud)
        
    return render(request, 'civilStud/update.html', {'form': form, 'profile': civil_stud})
def update4(request, id):
    form=Year4Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        civil_stud = civilStud4.objects.get(id=id)
    except civilStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/civil/year4/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year4Form(request.POST, instance=civil_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/civil/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year4Form(instance=civil_stud)
        
    return render(request, 'civilStud/update.html', {'form': form, 'profile': civil_stud})



# SEARCH


def search(request):
    if request.method=='GET':
        search=request.GET.get('search')
        post=civilStud.objects.all().filter(name=search)
        post2=civilStud2.objects.all().filter(name=search)
        post3=civilStud3.objects.all().filter(name=search)
        post4=civilStud4.objects.all().filter(name=search)
    return render(request,'civilStud/search.html',{'post':post,'post2':post2,'post3':post3,'post4':post4})

# CREATE

def create1(request):
    form=Year1Form()
    if request.method=='POST':
        form=Year1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/civil/year1/')    
    return render(request,'civilStud/create1.html',{'form':form})  

def create2(request):
    form=Year2Form()
    if request.method=='POST':
        form=Year2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/civil/year2/')    
    return render(request,'civilStud/create2.html',{'form':form})  
def create3(request):
    form=Year3Form()
    if request.method=='POST':
        form=Year3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/civil/year3/')    
    return render(request,'civilStud/create3.html',{'form':form})  
def create4(request):
    form=Year4Form()
    if request.method=='POST':
        form=Year4Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/civil/year4/')    
    return render(request,'civilStud/create4.html',{'form':form})  