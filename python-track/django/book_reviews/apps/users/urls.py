from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='landing'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^register$', views.user_register, name='register'),
    url(r'^users/(?P<user_id>\d+)/$', views.user_profile, name='user-profile'),
    url(r'^logout$', views.logout, name='logout')
]
