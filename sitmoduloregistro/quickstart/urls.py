from django.conf.urls import url, include
import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^logs', views.logs, name="logs"),
    # url(r'^', views.user_list, name='user_list'),
    url(r'^new', views.user_create, name='user_new'),
    url(r'^edit', views.user_update, name='user_edit'),
    url(r'^delete', views.user_delete, name='user_delete'),
    url(r'^view', views.user_view, name='user_view'),

    url(r'^expediente_new', views.expediente_create, name='expediente_new'),
    url(r'^expediente_edit', views.expediente_update, name='expediente_edit'),
    url(r'^expediente_delete', views.expediente_delete, name='expediente_delete'),
    url(r'^expediente_view', views.expediente_view, name='expediente_view'),
    url(r'^expediente_complete', views.expediente_complete, name='expediente_complete'),

    url(r'^acta_new', views.acta_create, name='acta_new'),
    url(r'^acta_edit', views.acta_update, name='acta_edit'),
    url(r'^acta_delete', views.acta_delete, name='acta_delete'),
    url(r'^acta_view', views.acta_view, name='acta_view'),
]