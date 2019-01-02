from django.contrib import admin
from .models import Slider
from .models import Blog
# Register your models here.
class showUpdated(admin.ModelAdmin):
    list_display = ('header', 'updated')
    list_filter = ['updated']
    
admin.site.register(Slider)
admin.site.register(Blog, showUpdated)