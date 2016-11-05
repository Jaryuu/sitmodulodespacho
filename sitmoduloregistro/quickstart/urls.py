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

]