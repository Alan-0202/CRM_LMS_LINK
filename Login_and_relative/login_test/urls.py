from django.conf.urls import url, include
from login_test import views
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login$', views.login),
    url(r'^login_check', views.login_check),
    url(r'^login_check_ajax', views.login_check_ajax),
    url(r'^list$', views.book_list),
    url(r'^prov$', views.prov),
]


