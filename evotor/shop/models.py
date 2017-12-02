from django.db import models
from util.model import BaseModel
from org.models import Organization


class Shop(BaseModel):
    title = models.CharField(max_length=50, unique=True)
    organization = models.ForeignKey(Organization, related_name="+")


class ProductTag(BaseModel):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title

    def _dto(self, public):
        return {
            "id": self.id,
            "title": self.title,
        }


class Product(BaseModel):
    bar_code = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(ProductTag, related_name="+", blank=True)
    delivery_date = models.DateTimeField(null=True, default=None)
    price = models.FloatField()
    cost_price = models.FloatField()
    count = models.IntegerField(default=0)

    def _dto(self, public):
        return {
            "id": self.id,
            "bar_code": self.bar_code,
            "title": self.title,
            "delivery_date": self.delivery_date,
            "tags": list(sorted(map(lambda tag: tag.title, self.tags.all()))),
            "price": "{:.2f}".format(self.price),
            "cost_price": "{:.2f}".format(self.cost_price),
            "count": self.count,
        }

    def __str__(self):
        return "{} ({})".format(self.title, self.bar_code)


class Provider(BaseModel):
    title = models.CharField(max_length=30, unique=True)
    products = models.ManyToManyField(Product, related_name="+", blank=True)

    def __str__(self):
        return self.title

    def _dto(self, public):
        return {
            "id": self.id,
            "title": self.title,
        }


class Purchase(BaseModel):
    product = models.ForeignKey(Product, related_name="+")
    status = models.CharField(max_length=20, default="ok")
    price = models.FloatField()
    dt = models.DateTimeField()

    def _dto(self, public):
        return {
            "id": self.id,
            "product": self.product.public_dto(),
            "status": self.status,
            "price": self.price,
            "dt": self.dt,
        }
