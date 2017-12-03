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
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@safe_view
def products_view(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    params = QueryParams.parse(request)
    params.filter.update(shop=shop)
    products = exec_query_raw(params, Product)

    shop_data = {}
    t = []
    if shop.data_id and os.path.isdir(BASE_DIR + '/data/successes/' + shop.data_id):
        for p in products:
            t += [int(p.bar_code)]
            fname = BASE_DIR + '/data/successes/' + shop.data_id + '/' + p.bar_code + '.csv'
            if p.bar_code and os.path.isfile(fname):
                shop_data[p.bar_code] = {}

                df = pd.read_csv(fname)
                shop_data[p.bar_code]['rest'] = list(map(float, df.iloc[:,0].values))
                shop_data[p.bar_code]['values'] = list(map(float, df.iloc[:,1].values))
                shop_data[p.bar_code]['is_pred'] = list(map(bool, df.iloc[:,2].values))

    # raise RuntimeError([shop.data_id, ''] + sorted(t))
    output = extract_suggests(shop.data_id)

    return render(request, "shop/products.html", {
        "products": products,
        "shop": shop,
        "shop_id": shop_id,
        "shop_data": shop_data,
        "suggests": output,
        # "has_data": list(shop_data.keys())
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


@safe_view
def get_suggests(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    output = extract_suggests(shop.data_id)

    return render(request, "shop/suggests.html", {
        "suggests": output
    })

def extract_suggests(shop_id):
    output = []

    suggests = pd.read_csv("suggests_for_shops.csv")
    vals = pd.read_csv("items_to_add.csv").values
    id_to_name = dict(list(zip(vals[:, 0], vals[:, 1])))

    items = list(filter(lambda x: x > 0, list(suggests[shop_id])))
    names = list(map(lambda x: id_to_name[x], items))
    for item, name in zip(items, names):
        output += [("suggest", item, name)]

    try:
        with open(str(shop_id) + ".csv", "r") as f:
            output += [("pair", list(map(lambda x: x.split(",", maxsplit=1), f.readlines())))]
    except:
        pass

    illiquid = pd.read_csv("illiquid.csv")
    temp = illiquid[illiquid["shop_id"] == int(shop_id)]
    items = temp["good_id"].values
    scores = temp["score"].values

    for good_id, score in zip(items, scores):
        output += [("ill", good_id, score, Product.objects.all().filter(bar_code=good_id).get())]

    return output

def extract_warnings(shop_id, type_):
    shop = Shop.objects.get(id=shop_id)
    empty_products = Product.objects.filter(shop_id=shop_id)

    return output
