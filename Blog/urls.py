from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = "Blog"),
    path('post/', views.post, name = "Post"),
]