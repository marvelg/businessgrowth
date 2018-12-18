from django.shortcuts import render, get_object_or_404
from .models import Slider
from .models import Blog
from django.core.paginator import Paginator
# Create your views here.
def blog(request):
    posts = Blog.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    slider = Slider.objects

    return render(request, 'Blog/Blog.html', {"Slider":slider, "posts" : posts, "blog_page" : "active"})

def post(request, blog_id):
    slider = Slider.objects
    posts = Blog.objects.all()
    post = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'Blog/Post.html', {"Blog" : post, "posts" : posts, "Slider":slider, "blog_page" : "active"})