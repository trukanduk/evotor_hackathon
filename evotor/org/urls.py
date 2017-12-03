from django.conf.urls import url, include
import org.views

urlpatterns = [
    url(r'^$', org.views.organization_index_view),
    url(r'^collaborators/$', org.views.collaborators_view),
    url('^register_api/$', org.views.register_api_view),
    url('^activate/(?P<activation_id>[a-zA-Z0-9]{20,30})/$', org.views.activate_view),
    url('^add_manager/$', org.views.add_manager_view),
    url('^manager_rights/(?P<manager_id>[0-9]{1,})/$', org.views.manager_rights_view),
    url('^manager_rights/(?P<manager_id>[0-9]{1,})/add/$', org.views.manager_rights_add_view),
    url('^manager_rights/delete/(?P<right_id>[0-9]{1,})/$', org.views.manager_rights_delete_view),
    url('^', include('django.contrib.auth.urls')),
]
