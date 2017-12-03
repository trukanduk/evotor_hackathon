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
    org = Organization.objects.get_or_create(title="Организация Кофейня")[0]
    print(org)

    if not User.objects.filter(username="kofeyana_owner").exists():
        owner = User.objects.create_user("kofeyana_owner", "owner@kofe.ru", "123")
        owner.first_name = "Иван"
        owner.last_name = "Кофееввич"
        owner.organization = org
        owner.role = User.Role.ADMIN
        owner.save()
    else:
        owner = User.objects.get(username="kofeyana_owner")


    if not Shop.objects.filter(organization=org).exists():
        shop = Shop.objects.create(
            organization=org,
            title="Кофейня",
            data_id=17846
        )
    else:
        shop = Shop.objects.get(organization=org)

    products = pd.read_csv("kofe.csv").values

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
    org = Organization.objects.get_or_create(title="Организация Пиво")[0]
    print(org)

    owner = User.objects.create_user("pivo_owner", "owner@pivo.ru", "123")
    owner.first_name = "Иван"
    owner.last_name = "Пивовар"
    owner.organization = org
    owner.role = User.Role.ADMIN
    owner.save()

    shop = Shop.objects.create(
        organization=org,
        title="Пиво",
        data_id=17846
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
    org = Organization.objects.get_or_create(title="Организация Водка")[0]
    print(org)

    owner = User.objects.create_user("vodka_owner", "owner@alco.ru", "123")
    owner.first_name = "Иван"
    owner.last_name = "Водочный"
    owner.organization = org
    owner.role = User.Role.ADMIN
    owner.save()

    shop = Shop.objects.create(
        organization=org,
        title="Алко",
        data_id=17846
    )

    products = pd.read_csv("alco.csv").values

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
    org = Organization.objects.get_or_create(title="Продуктовый магазин")[0]
    print(org)

    owner = User.objects.create_user("product_owner", "owner@product.ru", "123")
    owner.first_name = "Иван"
    owner.last_name = "Продуктовый"
    owner.organization = org
    owner.role = User.Role.ADMIN
    owner.save()

    shop = Shop.objects.create(
        organization=org,
        title="Продуктовый",
        data_id=17846
    )

    products = pd.read_csv("prod.csv").values

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
    org = Organization.objects.get_or_create(title="Мясная лавка")[0]
    print(org)

    owner = User.objects.create_user("meat_owner", "owner@meat.ru", "123")
    owner.first_name = "Иван"
    owner.last_name = "Мяснов"
    owner.organization = org
    owner.role = User.Role.ADMIN
    owner.save()

    shop = Shop.objects.create(
        organization=org,
        title="Мясной",
        data_id=17846
    )

    products = pd.read_csv("meat.csv").values

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
    org = Organization.objects.get_or_create(title="Ларек")[0]
    print(org)

    owner = User.objects.create_user("larek_owner", "owner@larek.ru", "123")
    owner.first_name = "Иван"
    owner.last_name = "Ларьковый"
    owner.organization = org
    owner.role = User.Role.ADMIN
    owner.save()

    shop = Shop.objects.create(
        organization=org,
        title="Ларек",
        data_id=17846
    )

    products = pd.read_csv("larek.csv").values

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

kofe()
pivo()
alco()
regular()
meat()
larek()