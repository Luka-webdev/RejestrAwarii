from django import forms
from . models import Awaria


class AwariaForm(forms.ModelForm):
    class Meta:
        model = Awaria
        fields = "__all__"
