from django.contrib import admin
from .models import whyChooseUs
from .models import Link
from .models import Address
from .models import Detail
# Register your models here.

class Static(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(whyChooseUs)
admin.site.register(Link)
admin.site.register(Address, Static)
admin.site.register(Detail)