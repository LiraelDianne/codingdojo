from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_dash, name='user-dash'),
    url(r'^admin/$', views.admin_dash, name='admin-dash')
]
