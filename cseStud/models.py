from django.db import models

# Create your models here.

class cseStud(models.Model):
    registerNo=models.CharField(max_length=11)
    name=models.CharField(max_length=20)
    rollno=models.CharField(max_length=6)
    Year=models.IntegerField()
    Class=models.CharField(max_length=10)
    DOB=models.DateField()
    Place=models.CharField(max_length=20)
    FirstGraduate=models.BooleanField()
    YearOfJoin=models.IntegerField()
    Languages=models.CharField(max_length=100)
    FatherName=models.CharField(max_length=20)
    FathersOccupation=models.CharField(max_length=20)
    MotherName=models.CharField(max_length=20)
    MothersOccupation=models.CharField(max_length=20)
    Fees=models.IntegerField()
    Pending=models.BooleanField()