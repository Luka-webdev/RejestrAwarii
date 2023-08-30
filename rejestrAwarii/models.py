from django.db import models
from django.utils.timezone import now


class Awaria(models.Model):
    Maszyny = [
        ("Tp3", "TruPunch 3000"),
        ("Tp4", "TruPunch 4000"),
        ("Tp5", "TruPunch 5000"),
        ("Kimla", "Laser Kimla"),
        ("HSG", "Laser HSG"),
        ("M1", "Durma M1"),
        ("M2", "Durma M2"),
        ("Cma", "Cma"),
        ("Crippa", "Giętarka Crippa"),
        ("Adr", 'Durma Adr'),
    ]
    Statusy = [
        ("W toku", "W toku"),
        ("Zakończone", "Zakończone")
    ]
    Alerty = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3")
    ]
    maszyna = models.CharField(choices=Maszyny, max_length=30)
    opis_usterki = models.TextField()
    zgłaszający = models.CharField(max_length=40)
    data = models.DateTimeField(default=now)
    stopień_alertu = models.CharField(max_length=50, choices=Alerty)
    status = models.CharField(
        choices=Statusy, default="W toku", max_length=20)
    naprawił = models.CharField(max_length=40)
    uwagi = models.TextField()
