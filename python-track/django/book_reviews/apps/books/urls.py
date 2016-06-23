from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='books'),
    url(r'^add$', views.add_book, name='add-book'),
    url(r'^create$', views.create_book, name='create-book'),
    url(r'^(?P<book_id>\d+)/$', views.display_book, name='display-book'),
    url(r'^(?P<book_id>\d+)/review$', views.add_review, name='add-review')
]
