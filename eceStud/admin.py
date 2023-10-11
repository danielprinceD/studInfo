from django.contrib import admin
from .models import eceStud,eceStud2,eceStud3,eceStud4
# Register your models here.

class eceAdmin(admin.ModelAdmin):
    l='__all__'
    
    
admin.site.register(eceStud,eceAdmin)
admin.site.register(eceStud2,eceAdmin)
admin.site.register(eceStud3,eceAdmin)
admin.site.register(eceStud4,eceAdmin)