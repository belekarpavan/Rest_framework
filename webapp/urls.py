

from django.contrib import admin
from django.urls import path,include
from webapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

rout=routers.DefaultRouter()
rout.register('emp/', views.pavan)


urlpatterns = [
    path('',include(rout.urls))
]