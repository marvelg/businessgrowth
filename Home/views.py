from django.shortcuts import render, get_object_or_404

from .models import Welcome
# Create your views here.
def home(request):
    welcome = Welcome.objects
    return render(request, 'Home/Home.html', {"Welcome": welcome})

def bio(request):
    return render(request, 'Home/Bio.html')