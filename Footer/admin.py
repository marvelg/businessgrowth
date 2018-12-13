from django.contrib import admin
from .models import Link
from .models import Address
from .models import Detail
# Register your models here.
class noAdd(admin.ModelAdmin):
    def has_add_permission(self,request):
        return False

admin.site.register(Link)
admin.site.register(Address, noAdd)
admin.site.register(Detail)