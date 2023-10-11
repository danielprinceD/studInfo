from django.contrib import admin
from .models import eeeStud,eeeStud2,eeeStud3,eeeStud4
# Register your models here.

class eeeAdmin(admin.ModelAdmin):
    l='__all__'
    
    
admin.site.register(eeeStud,eeeAdmin)
admin.site.register(eeeStud2,eeeAdmin)
admin.site.register(eeeStud3,eeeAdmin)
admin.site.register(eeeStud4,eeeAdmin)