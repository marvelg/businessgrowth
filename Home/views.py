from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home/Home.html')

def bio(request):
    return render(request, 'Home/Bio.html')