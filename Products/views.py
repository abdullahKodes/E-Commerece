from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all-products.html', {
        'products': products,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)
    return render(request, 'products/product-detail.html', {
        'product': product,
        'related_products': related_products,
    })
