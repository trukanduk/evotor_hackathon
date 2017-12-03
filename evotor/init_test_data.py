#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evotor.settings")
import django
django.setup()

import datetime
import random

from org.models import (
    Organization,
    User,
)
from shop.models import (
    Shop,
    UserShop,
    Product,
    ProductTag,
)


last_names = ["Абрамов", "Авдеев", "Агафонов", "Аксёнов", "Александров", "Алексеев",
"Андреев", "Анисимов", "Антонов", "Артемьев", "Архипов", "Афанасьев", "Баранов",
"Белов", "Белозёров", "Белоусов", "Беляев", "Беляков", "Беспалов", "Бирюков", "Блинов",
"Блохин", "Бобров", "Бобылёв", "Богданов", "Большаков", "Борисов", "Брагин", "Буров","Быков",
"Васильев", "Веселов", "Виноградов", "Вишняков", "Владимиров", "Власов", "Волков", "Воробьёв",
"Воронов", "Воронцов", "Гаврилов", "Галкин", "Герасимов", "Голубев", "Горбачёв", "Горбунов",
"Гордеев", "Горшков", "Григорьев", "Гришин", "Громов", "Гуляев", "Гурьев", "Гусев", "Гущин",
"Давыдов", "Данилов", "Дементьев", "Денисов", "Дмитриев", "Доронин", "Дорофеев", "Дроздов",
"Дьячков", "Евдокимов", "Евсеев", "Егоров", "Елисеев", "Емельянов", "Ермаков", "Ершов", "Ефимов",
"Ефремов", "Жданов", "Жуков", "Журавлёв", "Зайцев", "Захаров", "Зимин", "Зиновьев", "Зуев", "Зыков",
"Иванков", "Иванов", "Игнатов", "Игнатьев", "Ильин", "Исаев", "Исаков", "Кабанов", "Казаков",
"Калашников", "Калинин", "Капустин", "Карпов", "Кириллов", "Киселёв", "Князев", "Ковалёв", "Козлов",
"Колесников", "Колобов", "Комаров", "Комиссаров", "Кондратьев", "Коновалов", "Кононов", "Константинов",
"Копылов", "Корнилов", "Королёв", "Костин", "Котов", "Кошелев", "Красильников", "Крылов", "Крюков",
"Кудрявцев", "Кудряшов", "Кузнецов", "Кузьмин", "Кулагин", "Кулаков", "Куликов", "Лаврентьев",
"Лазарев", "Лапин", "Ларионов", "Лебедев", "Лихачёв", "Лобанов", "Логинов", "Лукин", "Лыткин", "Макаров", "Максимов", "Мамонтов", "Марков", "Мартынов", "Маслов", "Матвеев", "Медведев", "Мельников", "Меркушев", "Миронов", "Михайлов", "Михеев", "Мишин", "Моисеев", "Молчанов", "Морозов", "Муравьёв", "Мухин", "Мышкин", "Мясников", "Назаров", "Наумов", "Некрасов", "Нестеров", "Никитин", "Никифоров", "Николаев", "Никонов", "Новиков", "Носков", "Носов", "Овчинников", "Одинцов", "Орехов", "Орлов", "Осипов", "Павлов", "Панов", "Панфилов", "Пахомов", "Пестов", "Петров", "Петухов", "Поляков", "Пономарёв", "Попов", "Потапов", "Прохоров", "Рогов", "Родионов", "Рожков", "Романов", "Русаков", "Рыбаков", "Рябов", "Савельев", "Савин", "Сазонов", "Самойлов", "Самсонов", "Сафонов", "Селезнёв", "Селиверстов", "Семёнов", "Сергеев", "Сидоров", "Силин", "Симонов", "Ситников", "Соболев", "Соколов", "Соловьёв", "Сорокин", "Степанов", "Стрелков", "Субботин", "Суворов", "Суханов", "Сысоев", "Тарасов", "Терентьев", "Тетерин", "Тимофеев", "Титов", "Тихонов", "Третьяков", "Трофимов", "Туров", "Уваров", "Устинов", "Фадеев", "Фёдоров", "Федосеев", "Федотов", "Филатов", "Филиппов", "Фокин", "Фомин", "Фомичёв", "Фролов", "Харитонов", "Хохлов", "Цветков", "Чернов", "Шарапов", "Шаров", "Шашков", "Шестаков", "Шилов", "Ширяев", "Шубин", "Щербаков", "Щукин", "Юдин","Яковлев", "Якушев", "Смирнов"]

first_names = ["Иоанн",
"Григорий",
"Бенедикт",
"Климент",
"Иннокентий",
"Лев",
"Пий",
"Стефан",
"Бонифаций",
"Урбан",
"Александр",
"Адриан",
"Павел",
"Целестин",
"Николай",
"Сикст",]


def get_last_name():
    return random.choice(last_names)


def get_first_name():
    return random.choice(first_names)


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


def set_random_profit():
    shops = list(Shop.objects.all())
    
    for shop in shops:
        Shop.objects.filter(id=shop.id).update(
            week_profit=random.randint(-20000, 100000),
            month_profit=random.randint(-80000, 400000),
        )


def create_managers():
    shops = list(Shop.objects.all())
    for shop in shops:
        if not UserShop.objects.filter(shop=shop).exists():
            for i in range(random.randint(0, 7) // 5 + 1):
                username = "manager{}".format(random.randint(0, 10**15))
                user = User.objects.create_user(username, username + "@test.ru", "123")
                user.first_name = get_first_name()
                user.last_name = get_last_name()
                user.organization = shop.organization
                user.role = User.Role.MANAGER
                user.save()
                
                UserShop.objects.create(
                    user=user,
                    shop=shop,
                    type=UserShop.Role.READ_WRITE,
                )
                


#org1()
set_random_profit()
create_managers()
