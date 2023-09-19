from django import forms
from . models import Awaria
from django.core.exceptions import ValidationError


class AwariaForm(forms.ModelForm):

    class Meta:
        model = Awaria
        widgets = {
            'opis_usterki': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'uwagi': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AwariaForm, self).__init__(*args, **kwargs)
        # for key in self.fields:
        self.fields['naprawił'].required = False
        self.fields['uwagi'].required = False

    def clean(self):
        dane = super().clean()

        if dane['status'] == "W toku" and (dane['naprawił'] != "" or dane['uwagi'] != ""):
            raise ValidationError(
                "Jeżeli pole 'Status' ma wartość 'W toku' to pola 'Naprawił' i 'Uwagi' muszą być puste.")


Maszyny = [
    ("", "---"),
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
Alerty = [
    ("", "---"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3")
]


class Filtrowanie(forms.Form):
    wszystkie = forms.BooleanField(required=False, label="Pokaż wszystkie")
    maszyna = forms.ChoiceField(choices=Maszyny, required=False)
    zgłaszający = forms.CharField(required=False,)
    stopień_alertu = forms.ChoiceField(choices=Alerty, required=False)
    naprawił = forms.CharField(required=False, help_text=' ')
