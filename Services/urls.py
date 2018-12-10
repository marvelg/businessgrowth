from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name = "Services"),
    path('Product/', views.product, name = "Product"),
    path('Product-Description/', views.productdescription, name = "Product-Description"),
]
