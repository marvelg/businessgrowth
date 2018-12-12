from django.shortcuts import render
from .models import Segment
# Create your views here.
def about(request):
    segment = Segment.objects
    return render(request, 'About/About.html', {"Segment" : segment})