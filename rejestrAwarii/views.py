from django.shortcuts import render
from . models import Awaria
from . forms import AwariaForm


def ekranPowitalny(request):
    return render(request, 'rejestrAwarii/ekranPowitalny.html', {})


def nowaAwaria(request):
    if request.method != "POST":
        form = AwariaForm()
    else:
        form = AwariaForm(data=request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, 'rejestrAwarii/nowaAwaria.html', {'form': form})
