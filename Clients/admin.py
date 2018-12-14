from django.contrib import admin
from .models import Client
from .models import clientCategory
from .models import clientSlider
from .models import testimonialSlider
from .models import Testimonial
# Register your models here.
admin.site.register(clientSlider)
admin.site.register(Client)
admin.site.register(clientCategory)
admin.site.register(testimonialSlider)
admin.site.register(Testimonial)