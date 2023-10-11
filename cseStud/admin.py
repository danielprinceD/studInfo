from django.contrib import admin
from .models import cseStud,cseStud2,cseStud3,cseStud4
# Register your models here.

class cseAdmin(admin.ModelAdmin):
    l='__all__'
    
    
admin.site.register(cseStud,cseAdmin)
admin.site.register(cseStud2,cseAdmin)
admin.site.register(cseStud3,cseAdmin)
admin.site.register(cseStud4,cseAdmin)