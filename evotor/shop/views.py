from django.core.files.base import ContentFile
from django.http import HttpResponse
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
import pandas as pd


@safe_view
def products_view(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    params = QueryParams.parse(request)
    params.filter.update(shop=shop)
    products = exec_query_raw(params, Product)

    return render(request, "shop/products.html", {
        "products": products,
        "shop_id": shop_id
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


@safe_view
def get_excel(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    params = QueryParams.parse(request)
    params.filter.update(shop=shop)
    products = exec_query_raw(params, Product)

    to_df = []
    for product in products:
        d = product.__dict__
        del d["_state"]
        to_df += [d]

    pd.DataFrame(to_df).to_excel("temp.xls")

    with open("temp.xls", "rb") as f:
        string_to_return = f.read()

    file_to_send = ContentFile(string_to_return)
    response = HttpResponse(file_to_send, 'application/x-gzip')
    response['Content-Length'] = file_to_send.size
    response['Content-Disposition'] = 'attachment; filename="products.xls"'
    return response
