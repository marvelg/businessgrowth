from django.core.mail import EmailMessage, BadHeaderError, send_mail

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import ContactForm

import ctypes

from .models import Contact
from .models import Slider
from Footer.models import whyChooseUs

# Create your views here.
def contact(request):
    contact = Contact.objects
    slider = Slider.objects
    whychooseus = whyChooseUs.objects
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            subject = request.POST.get('subject', '')
            form_content = request.POST.get('content', '')
            
            # Email the profile with the
            # contact information
            template = get_template('Contact/contact_template.txt')
                
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'subject': subject,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            response = "Thank you for your message!"
            return render(request, "Contact/Contact.html", {"Contact" : contact, "Slider" : slider, "whyChooseUs" : whychooseus, "form" : form_class, "contact_page" : "active", "message" : response})
            
    return render(request, "Contact/Contact.html", {"Contact" : contact, "Slider" : slider, "whyChooseUs" : whychooseus, "form" : form_class, "contact_page" : "active"})