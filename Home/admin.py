from django.contrib import admin

from .models import Welcome
from .models import Slider
from .models import bestService
# Register your models here.
class noAdd(admin.ModelAdmin):
     def has_add_permission(self, request):
        return False

admin.site.register(Welcome, noAdd)
admin.site.register(Slider)
admin.site.register(bestService)
