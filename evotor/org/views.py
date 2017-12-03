from django.shortcuts import render
from org.utils import (
    get_user_shops,
)
from shop.models import (
    UserShop,
)


def organization_index_view(request):
    user_shops = get_user_shops(request.user)
    for us in user_shops:
        us.shop.managers = list(map(lambda us: us.user, UserShop.objects.filter(shop=us.shop, type=UserShop.Role.READ_WRITE)))
        if us.shop.week_profit < 0:
            us.shop.week_profit_type = "negative"
        else:
            us.shop.week_profit_type = "positive"
        if us.shop.month_profit < 0:
            us.shop.month_profit_type = "negative"
        else:
            us.shop.month_profit_type = "positive"
    
    return render(request, "org/index.html", {
        "user_shops": user_shops,
    })
