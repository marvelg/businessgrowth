from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

from .models import Contact
from .models import Slider


# Create your views here.
def contact(request):
    contact = Contact.objects
    slider = Slider.objects
    return render(request, "Contact/Contact.html", {"Contact" : contact, "Slider" : slider})