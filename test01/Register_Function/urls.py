from django.conf.urls import url

from Register_Function import views

urlpatterns = [
    url(r'^index', views.index),
]