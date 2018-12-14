from django.shortcuts import render
from .models import Segment
from .models import Slider
# Create your views here.
def about(request):
    segment = Segment.objects
    slider = Slider.objects
    return render(request, 'About/About.html', {"Segment" : segment, "Slider": slider})