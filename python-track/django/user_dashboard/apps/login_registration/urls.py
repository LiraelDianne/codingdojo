from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='login-reg-index'),
    url(r'^login$', views.loginUser, name='login'),
    url(r'^register$', views.registerUser, name='register'),
    url(r'^success$', views.success, name='login-reg-success')
]
