from django.shortcuts import render
from .models import Contact
# Create your views here.
def contact(request):
    contact = Contact.objects
    return render(request, "Contact/Contact.html", {"Contact" : contact})