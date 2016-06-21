from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='landing'),
    url(r'^login$', views.loginForm, name='login'),
    url(r'^register$', views.registerForm, name='register'),
    url(r'^login/process$', views.loginUser, name='login-user'),
    url(r'^register/process$', views.registerUser, name='register-user'),
    url(r'^success$', views.success, name='login-reg-success')
]
