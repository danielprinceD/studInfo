from django.contrib import admin
from .models import cseStud

# Register your models here.

class cseAdmin(admin.ModelAdmin):
    l=['registerNo','name','rollno','Year','Class','DOB','Place','FirstGraduate','YearOfJoin','Languages','FatherName','FathersOccupation','MotherName','MothersOccupation','Fees','Pending']
