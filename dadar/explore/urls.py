__author__ = 'erfan'

from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^init/(?P<location>([0-9]+)\.([0-9]+),([0-9]+)\.([0-9]+))', views.init)
]
