from django.shortcuts import render, get_object_or_404

from .models import Home
# Create your views here.
def home(request):
    home = Home.objects
    return render(request, 'Home/Home.html', {"Home": home})

def bio(request):
    return render(request, 'Home/Bio.html')