from django.urls import path,include
from . import views


appname='formare'
urlpatterns = [
    path('', views.index),
    path('contato/', views.contato),

]