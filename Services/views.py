from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'Services/Services.html')

def product(request):
    return render(request, 'Services/Product.html')

def productdescription(request):
    return render(request, 'Services/Product-Description.html')