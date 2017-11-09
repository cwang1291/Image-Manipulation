from django.conf.urls import url

from imageApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^image/$', views.handleCRUD, name="handleCRUD"),
    url(r'^image/(?P<id>\d+)', views.handleCRUD, name="handleCRUD"),
]


