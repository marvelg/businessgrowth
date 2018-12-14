from django.shortcuts import render
from .models import Gallery
from .models import Certificate
from .models import Slider
# Create your views here.
def gallery(request):
    slider = Slider.objects
    gallery = Gallery.objects
    certificate = Certificate.objects
    return render(request, "Gallery/Gallery.html", {"Gallery" : gallery, "Certificate" : certificate, "Slider" : slider})

