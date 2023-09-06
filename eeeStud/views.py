
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
