from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "Home"),
    path('<int:Founder_id>/',views.bio, name = "Bio")
]