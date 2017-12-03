from django.conf.urls import url, include
import org.views

urlpatterns = [
    url(r'^$', org.views.organization_index_view),
    url('^', include('django.contrib.auth.urls')),
]
