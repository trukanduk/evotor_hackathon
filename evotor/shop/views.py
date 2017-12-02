from django.shortcuts import render
from shop.models import (
    Product,
    Provider,
    Purchase,
)


def products_view(request):
    products = Product.objects.all()

    return render(request, "shop/products.html", {
        "products": products,
    })


def providers_view(request):
    providers = Provider.objects.all()

    return render(request, "shop/providers.html", {
        "providers": providers,
    })


def purchases_view(request):
    purchases = Purchase.objects.all()

    return render(request, "shop/purchases.html", {
        "purchases": purchases,
    })
