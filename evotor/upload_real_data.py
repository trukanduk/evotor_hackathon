#!/usr/bin/env python
import os
import pandas as pd

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
    Product
)


def kofe():
    if not Shop.objects.filter(organization=org).exists():
        shop = Shop.objects.create(
            organization=org,
            title="Кофейня",
            data_id=17846
        )
    else:
        shop = Shop.objects.get(organization=org)

    products = pd.read_csv("newkofe.csv").values

    for product in products:
        if not Product.objects.filter(shop=shop, title=product).exists():
            p = Product.objects.create(
                bar_code=product[0],
                title=product[1],
                shop=shop,
                delivery_date=datetime.datetime.now(),
                price=float(product[2]),
                cost_price=float(product[3]),
                count=int(product[4]))


def pivo():
    shop = Shop.objects.create(
        organization=org,
        title="Пиво",
        data_id=23293
    )

    products = pd.read_csv("pivo.csv").values

    for product in products:
        if not Product.objects.filter(shop=shop, title=product).exists():
            p = Product.objects.create(
                bar_code=product[0],
                title=product[1],
                shop=shop,
                delivery_date=datetime.datetime.now(),
                price=float(product[2]),
                cost_price=float(product[3]),
                count=int(product[4]))

def alco():
    shop = Shop.objects.create(
        organization=org,
        title="Алко",
        data_id=10171
    )

    products = pd.read_csv("newalco.csv").values

    for product in products:
        if not Product.objects.filter(shop=shop, title=product).exists():
            p = Product.objects.create(
                bar_code=product[0],
                title=product[1],
                shop=shop,
                delivery_date=datetime.datetime.now(),
                price=float(product[2]),
                cost_price=float(product[3]),
                count=int(product[4]))


def regular():
    shop = Shop.objects.create(
        organization=org,
        title="Продуктовый",
        data_id=11013
    )

    products = pd.read_csv("newprod.csv").values

    for product in products:
        if not Product.objects.filter(shop=shop, title=product).exists():
            p = Product.objects.create(
                bar_code=product[0],
                title=product[1],
                shop=shop,
                delivery_date=datetime.datetime.now(),
                price=float(product[2]),
                cost_price=float(product[3]),
                count=int(product[4]))

def meat():
    shop = Shop.objects.create(
        organization=org,
        title="Мясной",
        data_id=58864
    )

    products = pd.read_csv("newmeat.csv").values

    for product in products:
        if not Product.objects.filter(shop=shop, title=product).exists():
            p = Product.objects.create(
                bar_code=product[0],
                title=product[1],
                shop=shop,
                delivery_date=datetime.datetime.now(),
                price=float(product[2]),
                cost_price=float(product[3]),
                count=int(product[4]))


def larek():
    shop = Shop.objects.create(
        organization=org,
        title="Ларек",
        data_id=108664
    )

    products = pd.read_csv("newlarek.csv").values

    for product in products:
        if not Product.objects.filter(shop=shop, title=product).exists():
            p = Product.objects.create(
                bar_code=product[0],
                title=product[1],
                shop=shop,
                delivery_date=datetime.datetime.now(),
                price=float(product[2]),
                cost_price=float(product[3]),
                count=int(product[4]))

org = Organization.objects.get_or_create(title="Тестовая организация")[0]
print(org)

owner_filter = User.objects.filter(username="test")
if owner_filter.exists():
    owner = owner_filter[0]
else:
    owner = User.objects.create_user("test", "test@test.ru", "123")
    owner.first_name = "Тестовый"
    owner.last_name = "Аккаунт"
    owner.organization = org
    owner.role = User.Role.ADMIN
    owner.save()


kofe()
pivo()
alco()
regular()
meat()
larek()