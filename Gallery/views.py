from django.shortcuts import render
from .models import Gallery
from .models import Certificate
from .models import imagesSlider
from .models import videosSlider
from .models import Video
from Footer.models import whyChooseUs
# Create your views here.
def gallery(request):
    slider = imagesSlider.objects
    gallery = Gallery.objects
    certificate = Certificate.objects
    return render(request, "Gallery/Gallery.html", {"Gallery" : gallery, "Certificate" : certificate, "imagesSlider" : slider, "gallery_page" : "active"})

def videos(request):
    slider = videosSlider.objects
    video = Video.objects
    whychooseus = whyChooseUs.objects
    return render(request, "Gallery/Videos.html", {"videosSlider" : slider,"Video": video, "whyChooseUs" : whychooseus, "gallery_page" : "active"})