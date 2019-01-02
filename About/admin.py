from django.contrib import admin
from .models import Segment
from .models import Slider
# Register your models here.
class showCreated(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)


admin.site.register(Segment, showCreated)
admin.site.register(Slider)