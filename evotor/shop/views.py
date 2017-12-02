from django.shortcuts import render

# Create your views here.

def products_view(request):
    return render(request, "shop/products.html", {
        "products": [{
            "name": "product-{}".format(i),
        } for i in range(15)],
    })
