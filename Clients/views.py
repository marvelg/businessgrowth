from django.shortcuts import render

# Create your views here.
def clients(request):
    return render(request, 'Clients/Clients.html')

def testimonials(request):
    return render(request, 'Clients/Testimonials.html')