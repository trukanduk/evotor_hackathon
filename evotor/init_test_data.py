#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evotor.settings")
import django
django.setup()

import datetime

from org.models import (
    Organization,
    User,
)
from shop.models import (
    Shop,
    Product,
    ProductTag,
)


def get_tag(tag):
    return ProductTag.objects.get_or_create(title=tag)[0]


def org1():
    org = Organization.objects.get_or_create(title="Пятерочка")[0]
    print(org)

    owner_filter = User.objects.filter(username="serg")
    if owner_filter.exists():
        owner = owner_filter[0]
    else:
        owner = User.objects.create_user("serg", "serg@serg.ru", "123")
        owner.first_name = "Сергей"
        owner.last_name = "Сергеев"
        owner.organization = org
        owner.role = User.Role.ADMIN
        owner.save()

    with open("pytorochka_parsed.txt") as f:
        shops = f.read().split("\n")
        for shop in shops:
            if not shop:
                continue
            if not Shop.objects.filter(organization=org, title=shop).exists():
                Shop.objects.create(
                    organization=org,
                    title=shop,
                )

    shops = Shop.objects.filter(organization=org)
    
    products = (
        ("Пирожок", ("Еда", "Выпечка", "Не ешь его", "С капустой")),
        ("Виолончель", ("Без комментариев",)),
        ("Мячик", ("Мягкий",)),
        ("Огонь", ("О да", "Горячо")),
        ("Торт", ("Вкусный", "Шоколадный")),
        ("Стейк рибай", ("Самый настоящий", "Мясо")),
    )
    
    for shop in shops:
        for product in products:
            if not Product.objects.filter(shop=shop, title=product).exists():
                p = Product.objects.create(
                    bar_code=hash(product[0]),
                    title=product[0],
                    shop=shop,
                    delivery_date=datetime.datetime.now(),
                    price=20,
                    cost_price=13.3,
                    count=len(product[0]),
                )
                for tag in product[1]:
                    p.tags.add(get_tag(tag))

org1()
