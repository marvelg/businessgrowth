from django.shortcuts import render
from .models import Slider
from .models import Blog
# Create your views here.
def blog(request):
    slider = Slider.objects
    blog = Blog.objects
    return render(request, 'Blog/Blog.html', {"Slider":slider, "Blog":blog})

def post(request):
    return render(request, 'Blog/Post.html')