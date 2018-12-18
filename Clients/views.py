from django.shortcuts import render
from .models import Client
from .models import clientCategory
from .models import clientSlider
from .models import testimonialSlider
from .models import Testimonial
from Footer.models import whyChooseUs
from django.core.paginator import Paginator
# Create your views here.
def clients(request):
    clientslider = clientSlider.objects
    client = Client.objects
    clientcategory = clientCategory.objects
    return render(request, 'Clients/Clients.html', {"Client" : client, "clientCategory" : clientcategory, "clientSlider": clientslider, "clients_page" : "active"})

def testimonials(request):
    testimonial = Testimonial.objects.all()
    paginator = Paginator(testimonial, 5)
    page = request.GET.get('page')
    testimonial = paginator.get_page(page)

    testimonialslider = testimonialSlider.objects
    whychooseus = whyChooseUs.objects
    return render(request, 'Clients/Testimonials.html', {"testimonialSlider" : testimonialslider, "Testimonial": testimonial, "whyChooseUs" : whychooseus, "clients_page" : "active"})