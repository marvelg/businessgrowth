from django.shortcuts import render
from .models import Contact
from .models import Slider
# Create your views here.
def contact(request):
    contact = Contact.objects
    slider = Slider.objects
    return render(request, "Contact/Contact.html", {"Contact" : contact, "Slider" : slider})