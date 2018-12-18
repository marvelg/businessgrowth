from django.shortcuts import render
from .models import Segment
from .models import Slider
from Footer.models import whyChooseUs
# Create your views here.
def about(request):
    segment = Segment.objects
    slider = Slider.objects
    whychooseus = whyChooseUs.objects
    return render(request, 'About/About.html', {"Segment" : segment, "Slider": slider, "whyChooseUs" : whychooseus, "about_page" : "active"})