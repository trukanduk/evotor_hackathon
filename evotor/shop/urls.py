from django.conf.urls import url
import shop.views

urlpatterns = [
    url(r'^products/$', shop.views.products_view),
]
