from shop.models import (
    Shop,
    UserShop,
)


def get_user_shops_unsorted(user):
    if user.role == user.Role.ADMIN:
        return list(map(
            lambda shop: UserShop(
                user=user,
                shop=shop,
                type=UserShop.Role.READ_WRITE,
            ),
            Shop.objects.filter(organization=user.organization),
        ))

    if user.role == user.Role.TOP_MANAGER:
        title2user_shop = dict(map(
            lambda shop: shop.title, UserShop(
                user=user,
                shop=shop,
                type=UserShop.Role.READ,
            ),
            Shop.objects.filter(organization=user.organization),
        ))

        for user_shop in UserShop.objects.filter(user=request.user):
            title2user_shop[user_shop.title] = user_shop

        return list(title2user_shop.values())

    return list(sorted(UserShop.objects.filter(user=request.user), key=lambda us: us.shop.title))
    

def get_user_shops(user):
    return list(sorted(get_user_shops_unsorted(user), key=lambda us: us.shop.title))
