from django.shortcuts import render
from shop.models import (
    Shop,
    Product,
    Provider,
    Purchase,
)
from query_manager.utils import (
    exec_query,
    exec_query_raw,
    QueryParams,
)
from util.views import safe_view


@safe_view
def products_view(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    params = QueryParams.parse(request)
    params.filter.update(shop=shop)
    products = exec_query_raw(params, Product)

    return render(request, "shop/products.html", {
        "products": products,
    })


@safe_view
def providers_view(request):
    providers = exec_query(request, "provider")

    return render(request, "shop/providers.html", {
        "providers": providers,
    })


@safe_view
def purchases_view(request):
    purchases = exec_query(request, "purchase")

    return render(request, "shop/purchases.html", {
        "purchases": purchases,
    })
