from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_note$', views.add_note),
    url(r'^add_category$', views.add_category),
    url(r'^delete_category/(?P<id>\d+)$', views.delete_category),
    url(r'^delete_note/(?P<id>\d+)$', views.delete_note),
    url(r'^logout$', views.logout),
]