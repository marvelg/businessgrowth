from django.contrib import admin
from .models import Slider
from .models import Service
from .models import Product
# Register your models here.
class noAdd(admin.ModelAdmin):
     def has_add_permission(self, request):
        return False

admin.site.register(Slider, noAdd)
admin.site.register(Service)
admin.site.register(Product)