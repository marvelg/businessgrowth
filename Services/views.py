from django.shortcuts import render, get_object_or_404
from .models import Slider
from .models import Service
from .models import Product
# Create your views here.
def services(request):
    slider = Slider.objects
    service = Service.objects
    return render(request, 'Services/Services.html', {"Slider": slider, "Service" : service})

def product(request, product_id):
    Product_id = product_id
    service = Service.objects

    product = get_object_or_404(Service, pk = product_id)
    return render(request, 'Services/Product.html', {"Product" : product, "Service" : service, "product_id" : Product_id})

def productDescription(request, product_id, productDescription_id):
    Product_id = product_id
    service = Service.objects
    productDescription = get_object_or_404(Product, pk = productDescription_id)
    return render(request, 'Services/productDescription.html', {'Product' : productDescription, "Service" : service, "product_id" : Product_id})
    
    
def serviceProductDescription(request, product_id, serviceProductDescription_id):
    Product_id = product_id
    service = Service.objects
    productDescription = get_object_or_404(Service, pk = serviceProductDescription_id)
    return render(request, 'Services/serviceProductDescription.html', {'Product' : productDescription, "Service" : service, "product_id" : Product_id})

