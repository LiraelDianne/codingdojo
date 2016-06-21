from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='course-index'),
    url(r'^add/$', views.add, name='add-course'),
    url(r'^(?P<id>\d+)/delete/$', views.confirm, name='confirm-delete'),
    url(r'^delete_course/$', views.delete, name='delete-course'),
    url(r'^users_courses/$', views.display_users_courses, name='users-courses'),
    url(r'^add_user_to_course/$', views.add_user_course, name='add-user-course')
]
