from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'Blog/Blog.html')

def post(request):
    return render(request, 'Blog/Post.html')