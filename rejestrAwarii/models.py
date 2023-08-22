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
    maszyna = models.CharField(choices=Maszyny, blank=False, max_length=30)
    opis_userki = models.TextField(blank=False)
    zgłaszający = models.CharField(blank=False, max_length=40)
    data = models.DateTimeField(default=now, blank=False)
    stopień_alertu = models.CharField(max_length=50,
                                      blank=False, help_text="3 - maszyna nie działa, 2 - zagrożone poprawne działanie maszyny, 1 - rzecz do zrobienia")
    status = models.CharField(
        choices=Statusy, default="W toku", blank=False, max_length=20)
    naprawił = models.CharField(max_length=40)
    uwagi = models.TextField()
