from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name='get-products'),
    path('<str:pk>/', views.getProduct, name='get-product'),
]