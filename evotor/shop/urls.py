from django.conf.urls import url
import shop.views

urlpatterns = [
    url(r'^(?P<shop_id>[0-9]{1,30})/products/$', shop.views.products_view),
    url(r'^(?P<shop_id>[0-9]{1,30})/products/get-excel/$', shop.views.get_excel),
    url(r'^(?P<shop_id>[0-9]{1,30})/get_suggests/$', shop.views.get_suggests),
    url(r'^providers/$', shop.views.providers_view),
    url(r'^purchases/$', shop.views.purchases_view),
]
