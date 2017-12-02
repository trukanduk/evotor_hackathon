#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evotor.settings")
import django
django.setup()

from org.models import (
    Organization,
    User,
)
from shop.models import Shop


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


org1()
