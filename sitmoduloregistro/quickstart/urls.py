from django.conf.urls import url, include
import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^logs', views.logs, name="logs"),
    # url(r'^', views.user_list, name='user_list'),
    url(r'^new', views.user_create, name='user_new'),
    url(r'^edit/(?P<pk>\d+)', views.user_update, name='user_edit'),
    url(r'^delete/(?P<pk>\d+)', views.user_delete, name='user_delete'),

    url(r'^expediente/new', views.expediente_create, name='expediente_new'),
    url(r'^expediente/edit', views.expediente_update, name='expediente_edit'),
    url(r'^expediente/delete', views.expediente_delete, name='expediente_delete'),

    url(r'^acta/new', views.acta_create, name='acta_new'),
    url(r'^acta/edit', views.acta_update, name='acta_edit'),
    url(r'^acta/delete', views.acta_delete, name='acta_delete'),
]