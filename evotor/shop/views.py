from django.shortcuts import render
from shop.models import (
    Product,
    Provider,
)


def products_view(request):
    products = Product.objects.all()
    
    return render(request, "shop/products.html", {
        "products": map(Product.public_dto, products),
    })


def providers_view(request):
    providers = Provider.objects.all()
    
    return render(request, "shop/providers.html", {
        "providers": map(Provider.public_dto, providers),
    })
