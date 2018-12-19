from django.contrib import admin
from .models import Gallery
from .models import Certificate
from .models import imagesSlider
from .models import videosSlider
from .models import Video
# Register your models here.
class showCreated(admin.ModelAdmin):
    list_display = ('imageTitle', 'created', 'updated')
    list_filter = ('created','updated')


admin.site.register(imagesSlider)
admin.site.register(Gallery, showCreated)
admin.site.register(Certificate, showCreated)

admin.site.register(videosSlider)
admin.site.register(Video)