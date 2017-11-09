from django.conf.urls import url

from imageApp import views

urlpatterns = [
    url(r'^image/', views.handleGETandPOST, name="handleGETandPOST"),
    url(r'^image/([0-9]+)/?$', views.handlePUTandDELETE, name="handlePUTandDELETE"),
]


