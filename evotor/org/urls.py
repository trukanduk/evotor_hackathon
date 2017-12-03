from django.conf.urls import url, include
import org.views

urlpatterns = [
    url(r'^$', org.views.organization_index_view),
    url('^register_api/$', org.views.register_api_view),
    url('^activate/(?P<activation_id>[a-zA-Z0-9]{20,30})/$', org.views.activate_view),
    url('^', include('django.contrib.auth.urls')),
]
