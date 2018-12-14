from django.contrib import admin
from .models import Slider
from .models import Service
from .models import Product
# Register your models here.


class showCategory(admin.ModelAdmin):
        list_display = ('title','serviceCategory', 'updated')
        list_filter = ('serviceCategory',)

admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Product, showCategory)