from django.contrib import admin
from .models import civilStud,civilStud2,civilStud3,civilStud4
# Register your models here.

class civilAdmin(admin.ModelAdmin):
    l='__all__'
    
    
admin.site.register(civilStud,civilAdmin)