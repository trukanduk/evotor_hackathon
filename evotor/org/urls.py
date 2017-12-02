from django.conf.urls import url
import org.views

urlpatterns = [
    url(r'^$', org.views.organization_index_view),
]
