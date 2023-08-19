from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcomeScreen, name='welcomeScreen')
]
