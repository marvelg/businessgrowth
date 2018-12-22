from django.contrib import admin

from .models import Welcome
from .models import Slider
from .models import bestService
from .models import Founder
from .models import Client
from .models import Testimonial
from .models import internationalPartner
# Register your models here.
class Static(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Welcome,Static)
admin.site.register(Slider)
admin.site.register(bestService)
admin.site.register(Founder, Static)
admin.site.register(Client)
admin.site.register(Testimonial)
admin.site.register(internationalPartner)

admin.site.site_header = 'BusinessGrowth Admin'
