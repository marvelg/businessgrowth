from django.shortcuts import render
from .models import Client
from .models import clientCategory
from .models import clientSlider
from .models import testimonialSlider
from .models import Testimonial
# Create your views here.
def clients(request):
    clientslider = clientSlider.objects
    client = Client.objects
    clientcategory = clientCategory.objects
    return render(request, 'Clients/Clients.html', {"Client" : client, "clientCategory" : clientcategory, "clientSlider": clientslider})

def testimonials(request):
    testimonialslider = testimonialSlider.objects
    testimonial = Testimonial.objects
    return render(request, 'Clients/Testimonials.html', {"testimonialSlider" : testimonialslider, "Testimonial": testimonial})