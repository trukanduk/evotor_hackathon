from django.shortcuts import render
from org.utils import (
    get_user_shops,
)


def organization_index_view(request):
    user_shops = get_user_shops(request.user)
    print(len(user_shops))
    
    return render(request, "org/index.html", {
        "user_shops": user_shops,
    })
