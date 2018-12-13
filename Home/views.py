from django.shortcuts import render, get_object_or_404

from .models import Welcome
from .models import Slider
from .models import bestService
from .models import Founder
from .models import Client
from .models import Testimonial
from .models import internationalPartner

# Create your views here.
def home(request):
    welcome = Welcome.objects
    slider = Slider.objects
    bestservice = bestService.objects
    founder = Founder.objects
    client = Client.objects
    testimonial = Testimonial.objects
    internationalpartner = internationalPartner.objects
    return render(request, 'Home/Home.html', {"Welcome": welcome, "Slider" : slider, "bestService" : bestservice, "Founder" : founder, "Client" : client, "Testimonial" : testimonial, "internationalPartner" : internationalpartner})

def bio(request, Founder_id):
    founder = get_object_or_404(Founder, pk = Founder_id)
    return render(request, 'Home/Bio.html', {"Founder" : founder})