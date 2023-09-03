from django.shortcuts import render, redirect
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
            return redirect('ekranPowitalny')
    return render(request, 'rejestrAwarii/nowaAwaria.html', {'form': form})


def wToku(request):
    wpisy = Awaria.objects.all()
    return render(request, 'rejestrAwarii/wToku.html', {'wpisy': wpisy})


def edycjaWpisu(request, pk):
    wpis = Awaria.objects.get(id=pk)
    if request.method != 'POST':
        form = AwariaForm(instance=wpis)
    else:
        form = AwariaForm(instance=wpis, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('wToku')
    return render(request, 'rejestrAwarii/edycjaWpisu.html', {'wpis': wpis, 'form': form})
