import json
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from org.utils import (
    get_user_shops,
)
from shop.models import (
    UserShop,
)
from org.models import (
    User,
    Organization,
)
from util.utils import get_new_id


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


@csrf_exempt
def register_api_view(request):
    params = json.loads(request.body.decode("utf-8"))
    print(params)
    
    org = Organization.objects.create(
        title=params.get("org_name", ""),
        evotor_user_id=params.get("userId", ""),
    )

    email = params.get("email", "")
    password = 123
    user = User.objects.create_user(
        params.get("login", ""),
        email,
        password,
    )
    user.first_name = params.get("first_name", "")
    user.last_name = params.get("last_name", "")
    user.role = User.Role.ADMIN
    user.organization = org
    user.activation_link = get_new_id()
    user.save()
    
    send_mail(
        "{}, спасибо за регистрацию!".format(user.first_name),
        "Ссылка для входа в личный кабинет: http://evorot.kingbee.solutions/org/activate/{}/".format(user.activation_link),
        "admin@evorot.kingbee.solutions",
        [email],
    )
    
    return JsonResponse({
        "userId": org.evotor_user_id,
        "token": "123",
    })


def activate_view(request, activation_id):
    user = User.objects.get(activation_link=activation_id)
    
    if request.method == "POST":
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if password != confirm_password:
            raise Exception("password != password2")
        
        user.set_password(password)
        user.save()
        
        authenticate(username=user.username, password=password)

        return redirect("/org/")

    return render(request, "org/activation.html", {
    })
