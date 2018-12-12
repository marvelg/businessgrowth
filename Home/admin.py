from django.contrib import admin

from .models import Welcome
from .models import Slider
from .models import bestService
from .models import Founder
from .models import Client
from .models import Testimonial
from .models import internationalPartner
# Register your models here.
class noAdd(admin.ModelAdmin):
     def has_add_permission(self, request):
        return False

admin.site.register(Welcome, noAdd)
admin.site.register(Slider)
admin.site.register(bestService)
admin.site.register(Founder, noAdd)
admin.site.register(Client)
admin.site.register(Testimonial)
admin.site.register(internationalPartner)