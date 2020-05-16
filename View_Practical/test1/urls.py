from django.conf.urls import url, include
from test1 import views
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^ajax_test$', views.ajax_test),
    url(r'^ajax_handle$', views.ajax_handle)
]
