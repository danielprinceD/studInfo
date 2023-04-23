from django.db import models
from django.conf import settings
from django import forms

# Create your models here.

class cseStud(models.Model):
    registerNo=models.CharField(max_length=11,default=None,blank=True, null=True)
    name=models.CharField(max_length=20,default=None,blank=True, null=True)
    rollno=models.CharField(max_length=7,default=None,blank=True, null=True)
    Year=models.IntegerField(default=None,blank=True, null=True)
    Class=models.CharField(max_length=10,default=None,blank=True, null=True)
    DOB=models.DateField(default=None,blank=True, null=True)
    Place=models.CharField(max_length=20,default=None,blank=True, null=True)
    
    YearOfJoin=models.IntegerField(default=None,blank=True, null=True)
    Languages=models.CharField(max_length=100,default=None,blank=True, null=True)
    FatherName=models.CharField(max_length=20,default=None,blank=True, null=True)
    FathersOccupation=models.CharField(max_length=20,default=None,blank=True, null=True)
    MotherName=models.CharField(max_length=20,default=None,blank=True, null=True)
    MothersOccupation=models.CharField(max_length=20,default=None,blank=True, null=True)
    Fees=models.IntegerField(default=None,blank=True, null=True)
    
class cseStud2(models.Model):
    registerNo=models.CharField(max_length=11,default=None,blank=True, null=True)
    name=models.CharField(max_length=20,default=None,blank=True, null=True)
    rollno=models.CharField(max_length=7,default=None,blank=True, null=True)
    Year=models.IntegerField(default=None,blank=True, null=True)
    Class=models.CharField(max_length=10,default=None,blank=True, null=True)
    DOB=models.DateField(default=None,blank=True, null=True)
    Place=models.CharField(max_length=20,default=None,blank=True, null=True)
    
    YearOfJoin=models.IntegerField(default=None,blank=True, null=True)
    Languages=models.CharField(max_length=100,default=None,blank=True, null=True)
    FatherName=models.CharField(max_length=20,default=None,blank=True, null=True)
    FathersOccupation=models.CharField(max_length=20,default=None,blank=True, null=True)
    MotherName=models.CharField(max_length=20,default=None,blank=True, null=True)
    MothersOccupation=models.CharField(max_length=20,default=None,blank=True, null=True)
    Fees=models.IntegerField(default=None,blank=True, null=True)
    
class cseStud3(models.Model):
    registerNo=models.CharField(max_length=11,default=None,blank=True, null=True)
    name=models.CharField(max_length=20,default=None,blank=True, null=True)
    rollno=models.CharField(max_length=7,default=None,blank=True, null=True)
    Year=models.IntegerField(default=None,blank=True, null=True)
    Class=models.CharField(max_length=10,default=None,blank=True, null=True)
    DOB=models.DateField(default=None,blank=True, null=True)
    Place=models.CharField(max_length=20,default=None,blank=True, null=True)
    
    YearOfJoin=models.IntegerField(default=None,blank=True, null=True)
    Languages=models.CharField(max_length=100,default=None,blank=True, null=True)
    FatherName=models.CharField(max_length=20,default=None,blank=True, null=True)
    FathersOccupation=models.CharField(max_length=20,default=None,blank=True, null=True)
    MotherName=models.CharField(max_length=20,default=None,blank=True, null=True)
    MothersOccupation=models.CharField(max_length=20,default=None,blank=True, null=True)
    Fees=models.IntegerField(default=None,blank=True, null=True)
    
class cseStud4(models.Model):
    registerNo=models.CharField(max_length=11,default=None,blank=True, null=True)
    name=models.CharField(max_length=20,default=None,blank=True, null=True)
    rollno=models.CharField(max_length=7,default=None,blank=True, null=True)
    Year=models.IntegerField(default=None,blank=True, null=True)
    Class=models.CharField(max_length=10,default=None,blank=True, null=True)
    DOB=models.DateField(default=None,blank=True, null=True)
    Place=models.CharField(max_length=20,default=None,blank=True, null=True)
    
    YearOfJoin=models.IntegerField(default=None,blank=True, null=True)
    Languages=models.CharField(max_length=100,default=None,blank=True, null=True)
    FatherName=models.CharField(max_length=20,default=None,blank=True, null=True)
    FathersOccupation=models.CharField(max_length=20,default=None,blank=True, null=True)
    MotherName=models.CharField(max_length=20,default=None,blank=True, null=True)
    MothersOccupation=models.CharField(max_length=20,default=None,blank=True, null=True)
    Fees=models.IntegerField(default=None,blank=True, null=True)
    

def __str__(self):
    li=['registerNO','name']
    
    