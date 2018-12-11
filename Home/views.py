from django.shortcuts import render, get_object_or_404

from .models import Welcome
from .models import Slider
from .models import bestService
# Create your views here.
def home(request):
    welcome = Welcome.objects
    slider = Slider.objects
    bestservice = bestService.objects
    return render(request, 'Home/Home.html', {"Welcome": welcome, "Slider" : slider, "bestService" : bestservice})

def bio(request):
    return render(request, 'Home/Bio.html')