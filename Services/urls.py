from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name = "Services"),
    path('<int:product_id>/', views.product, name = "Product"),
    path('product/<int:product_id>/<int:serviceProductDescription_id>/', views.serviceProductDescription, name = "serviceProductDescription"),
    path('<int:product_id>/<int:productDescription_id>/', views.productDescription, name = "productDescription"),
    
]
