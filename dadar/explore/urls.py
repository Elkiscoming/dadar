__author__ = 'erfan'

from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^init/(?P<location>([0-9]+)\.([0-9]+),([0-9]+)\.([0-9]+))', views.init),
    url(r'^image/(?P<user_id>([0-9]+))/(?P<place_number>([0-9]+))', views.get_image)
]
