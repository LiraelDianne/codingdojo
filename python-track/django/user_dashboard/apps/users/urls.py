from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show/$', views.home_profile, name='home-profile'),
    url(r'^show/(?P<user_id>\d+)/$', views.user_profile, name='user-profile'),
    url(r'^message/()/$', views.post_message, name='message-user'),
    url(r'^comment/(?P<message_id>\d+)/(?P<user_id>\d+)/$', views.comment, name='comment'),
    url(r'^new/$', views.new_user, name='new-user'),
    url(r'^create/$', views.create_user, name='create-user'),
    url(r'^edit/$', views.edit_profile, name='edit-profile'),
    url(r'^edit/(?P<user_id>\d+)/$', views.edit_user, name='edit-user'),
    url(r'^update/(?P<user_id>\d+)/$', views.update_info, name='update-info'),
    url(r'^update/(?P<user_id>\d+)/password/$', views.update_pw, name='update-pw'),
    url(r'^update/(?P<user_id>\d+)/description/$', views.update_desc, name='update-desc'),
    url(r'^remove/(?P<user_id>\d+)/$', views.remove_user, name='remove-user')
]
