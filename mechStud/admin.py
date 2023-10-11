from django.contrib import admin
from .models import mechStud,mechStud2,mechStud3,mechStud4
# Register your models here.

class mechAdmin(admin.ModelAdmin):
    l='__all__'
    
    
admin.site.register(mechStud,mechAdmin)
admin.site.register(mechStud2,mechAdmin)
admin.site.register(mechStud3,mechAdmin)
admin.site.register(mechStud4,mechAdmin)