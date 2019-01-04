from django.shortcuts import render, get_object_or_404

from .models import Welcome
from .models import Slider
from .models import bestService
from .models import Founder
from .models import Client
from .models import Testimonial
from .models import internationalPartner
from Services.models import Service
from Footer.models import whyChooseUs
# Create your views here.
def home(request):
    welcome = Welcome.objects
    slider = Slider.objects
    bestservice = bestService.objects
    service = Service.objects
    founder = Founder.objects
    client = Client.objects
    testimonial = Testimonial.objects
    internationalpartner = internationalPartner.objects
    whychooseus = whyChooseUs.objects
    return render(request, 'Home/Home.html', {"Welcome": welcome, "Slider" : slider, "bestService" : bestservice, "Service": service, "Founder" : founder, "Client" : client, "Testimonial" : testimonial, "internationalPartner" : internationalpartner, "whyChooseUs" : whychooseus, "home_page" : "active"})

def bio(request, Founder_id):
    founder = get_object_or_404(Founder, pk = Founder_id)
    whychooseus = whyChooseUs.objects
    return render(request, 'Home/Bio.html', {"Founder" : founder, "whyChooseUs" : whychooseus})