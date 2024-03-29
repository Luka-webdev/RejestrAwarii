from django.urls import path
from . import views

urlpatterns = [
    path('', views.ekranPowitalny, name='ekranPowitalny'),
    path("nowaAwaria", views.nowaAwaria, name="nowaAwaria"),
    path("wToku", views.wToku, name="wToku"),
    path('edycjaWpisu/<int:pk>/', views.edycjaWpisu, name='edycjaWpisu'),
    path('zakończone', views.zakonczone, name="zakończone")
]
