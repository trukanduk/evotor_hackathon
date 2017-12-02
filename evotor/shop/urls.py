from django.conf.urls import url
import shop.views

urlpatterns = [
    url(r'^products/$', shop.views.products_view),
    url(r'^providers/$', shop.views.providers_view),
]
