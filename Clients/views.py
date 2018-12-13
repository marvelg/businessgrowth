from django.shortcuts import render
from .models import Client
from .models import clientCategory
# Create your views here.
def clients(request):
    client = Client.objects
    clientcategory = clientCategory.objects
    return render(request, 'Clients/Clients.html', {"Client" : client, "clientCategory" : clientcategory})

def testimonials(request):
    return render(request, 'Clients/Testimonials.html')