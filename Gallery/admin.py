from django.contrib import admin
from .models import Gallery
from .models import Certificate
from .models import Slider
# Register your models here.
class showCreated(admin.ModelAdmin):
    list_display = ('imageTitle', 'created', 'updated')
    list_filter = ('created','updated')


admin.site.register(Slider)
admin.site.register(Gallery, showCreated)
admin.site.register(Certificate, showCreated)
