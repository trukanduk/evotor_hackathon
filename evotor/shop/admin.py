from django.contrib import admin
from shop.models import (
    Shop,
    Product,
    ProductTag,
    Provider,
    Purchase,
)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("title", "organization",)


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "bar_code", "shop", "organization", "price", "count",)

    def organization(self, obj):
        return obj.shop.organization


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("product_title", "price", "dt",)
    
    def product_title(self, purchase):
        return purchase.product.title
