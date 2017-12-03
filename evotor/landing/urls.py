from django.conf.urls import url
import landing.views

urlpatterns = [
    url(r'^$', landing.views.landing_view),
]
