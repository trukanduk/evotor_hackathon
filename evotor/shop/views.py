from django.shortcuts import render
from shop.models import (
    Product,
)


def products_view(request):
    products = Product.objects.all()
    
    return render(request, "shop/products.html", {
        "products": map(Product.public_dto, products),
    })
