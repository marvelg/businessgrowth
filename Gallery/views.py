from django.shortcuts import render
from .models import Gallery
from .models import Certificate
# Create your views here.
def gallery(request):
    gallery = Gallery.objects
    certificate = Certificate.objects
    return render(request, "Gallery/Gallery.html", {"Gallery" : gallery, "Certificate" : certificate})

