from django.contrib import admin
from .models import civilStud,civilStud2,civilStud3,civilStud4
# Register your models here.

class civilAdmin(admin.ModelAdmin):
    l='__all__'
    
    
admin.site.register(civilStud,civilAdmin)
admin.site.register(civilStud2,civilAdmin)
admin.site.register(civilStud3,civilAdmin)
admin.site.register(civilStud4,civilAdmin)