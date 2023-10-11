from unicodedata import name
from django.shortcuts import render,redirect
from .models import cseStud
from .models import cseStud2 ,cseStud3,cseStud4
from .forms import Year1Form
from .forms import Year2Form
from .forms import Year3Form
from .forms import Year4Form

# Create your views here.

def cse(request):
    return render(request,'cseStud/year.html')
# YEAR 
def year1(request):
    data=cseStud.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/1year.html',context=sdata)

def year2(request):
    data=cseStud2.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/2year.html',context=sdata)

def year3(request):
    data=cseStud3.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/3year.html',context=sdata)

def year4(request):
    data=cseStud4.objects.all()
    sdata={'data':data}
    return render(request,'cseStud/4year.html',context=sdata)

# PROFILE


def profile(request,id):
    profil=cseStud.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile.html',context=pro)

def profile2(request,id):
    profil=cseStud2.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile2.html',context=pro)

def profile3(request,id):
    profil=cseStud3.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile3.html',context=pro)

def profile4(request,id):
    profil=cseStud4.objects.get(id=id)
    pro={'profile':profil}
    return render(request, 'cseStud/profile4.html',context=pro)


# DELETE

def delete(request,id):
    delet=cseStud.objects.get(id=id)
    delet.delete()
    return redirect('/cse/year1/')

def delete2(request,id):
    delet=cseStud2.objects.get(id=id)
    delet.delete()
    return redirect('/cse/year2/')

def delete3(request,id):
    delet=cseStud3.objects.get(id=id)
    delet.delete()
    return redirect('/cse/year3/')

def delete4(request,id):
    delet=cseStud4.objects.get(id=id)
    delet.delete()
    return redirect('/cse/year4/')
    

# UPDATE


def update(request, id):
    form=Year1Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        cse_stud = cseStud.objects.get(id=id)
    except cseStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/cse/year1/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year1Form(request.POST, instance=cse_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/cse/year1/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year1Form(instance=cse_stud)
        
    return render(request, 'cseStud/update.html', {'form': form, 'profile': cse_stud})
def update2(request, id):
    form=Year2Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        cse_stud = cseStud2.objects.get(id=id)
    except cseStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/cse/year2/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year2Form(request.POST, instance=cse_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/cse/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year2Form(instance=cse_stud)
        
    return render(request, 'cseStud/update.html', {'form': form, 'profile': cse_stud})


def update3(request, id):
    form=Year3Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        cse_stud = cseStud3.objects.get(id=id)
    except cseStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/cse/year3/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year3Form(request.POST, instance=cse_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/cse/year3/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year3Form(instance=cse_stud)
        
    return render(request, 'cseStud/update.html', {'form': form, 'profile': cse_stud})
def update4(request, id):
    form=Year4Form()
    try:
        # Get the student's profile using the provided 'id' parameter.
        cse_stud = cseStud4.objects.get(id=id)
    except cseStud.DoesNotExist:
        # Handle the case where the student profile does not exist.
        return redirect('/cse/year4/')  # Redirect to a proper page or show an error message

    if request.method == 'POST':
        # Create a form instance with data from the POST request and the retrieved student's profile.
        form = Year4Form(request.POST, instance=cse_stud)
        
        # Check if the submitted form data is valid.
        if form.is_valid():
            form.save()
            return redirect('/cse/year2/')  # Redirect after successful update
        print(form.cleaned_data)
    else:
        
        # Create a form instance with the student's profile data for displaying in the template.
        form = Year4Form(instance=cse_stud)
        
    return render(request, 'cseStud/update.html', {'form': form, 'profile': cse_stud})



# SEARCH


def search(request):
    if request.method=='GET':
        search=request.GET.get('search')
        post=cseStud.objects.all().filter(name=search)
        post2=cseStud2.objects.all().filter(name=search)
        post3=cseStud3.objects.all().filter(name=search)
        post4=cseStud4.objects.all().filter(name=search)
    return render(request,'cseStud/search.html',{'post':post,'post2':post2,'post3':post3,'post4':post4})

# CREATE

def create1(request):
    form=Year1Form()
    if request.method=='POST':
        form=Year1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cse/year1/')    
    return render(request,'cseStud/create1.html',{'form':form})  

def create2(request):
    form=Year2Form()
    if request.method=='POST':
        form=Year2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cse/year2/')    
    return render(request,'cseStud/create2.html',{'form':form})  
def create3(request):
    form=Year3Form()
    if request.method=='POST':
        form=Year3Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cse/year3/')    
    return render(request,'cseStud/create3.html',{'form':form})  
def create4(request):
    form=Year4Form()
    if request.method=='POST':
        form=Year4Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cse/year4/')    
    return render(request,'cseStud/create4.html',{'form':form})  