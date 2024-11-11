from django.shortcuts import render
from .models import Category
from Products.models import Product

# Create your views here.


def home(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    return render(request, 'categories/home.html', {
        'products': product,
        'categories': categories
    })


def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'categories/category_product.html', {
        'category': category,
        'products': products
    })
