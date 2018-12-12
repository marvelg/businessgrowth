from django.contrib import admin
from .models import Contact
# Register your models here.
class noAdd(admin.ModelAdmin):
     def has_add_permission(self, request):
        return False

admin.site.register(Contact, noAdd)