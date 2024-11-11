from django.urls import path
from . import views

urlpatterns = [
    path('products', views.all_products, name='all_products'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
]
