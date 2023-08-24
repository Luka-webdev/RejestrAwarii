from django.urls import path
from . import views

urlpatterns = [
    path('', views.ekranPowitalny, name='ekranPowitalny'),
    path("nowaAwaria", views.nowaAwaria, name="nowaAwaria")
]
