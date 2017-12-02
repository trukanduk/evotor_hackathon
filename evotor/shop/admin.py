from django.contrib import admin
from shop.models import (
    Product,
    ProductTag,
    Provider,
    Purchase,
)


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "count",)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("product_title", "price", "dt",)
    
    def product_title(self, purchase):
        return purchase.product.title
