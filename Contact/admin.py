from django.contrib import admin
from .models import Slider
from .models import Contact
# Register your models here.

class Static(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
        
admin.site.register(Slider)
admin.site.register(Contact)