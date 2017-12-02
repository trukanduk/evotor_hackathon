from django.contrib import admin
from shop.models import (
    Product,
    ProductTag,
)


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
