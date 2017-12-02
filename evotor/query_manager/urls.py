from django.conf.urls import url
import query_manager.views

urlpatterns = [
    url(r'^json/(?P<model_name>[a-zA-Z0-9_]{1,})/$', query_manager.views.json_query_view),
    url(r'^html/(?P<model_name>[a-zA-Z0-9_]{1,})/$', query_manager.views.html_query_view),
]
