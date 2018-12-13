from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name = "Services"),
    path('<int:product_id>/', views.product, name = "Product"),
    path('Product-Description/', views.productdescription, name = "Product-Description"),
]
