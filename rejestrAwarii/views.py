from django.shortcuts import render, redirect
from . models import Awaria
from . forms import AwariaForm, Filtrowanie


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
    wybranaMaszyna = None
    wszystkie = None
    dane = None
    wybranyZgłaszający = None
    wybranyAlert = None
    if request.method == "POST":
        form = Filtrowanie(request.POST)
        wybranaMaszyna = request.POST['maszyna']
        wszystkie = request.POST.get('wszystkie')
        wybranyZgłaszający = request.POST.get('zgłaszający')
        wybranyAlert = request.POST.get('stopień_alertu')
        if wszystkie == "on":
            dane = Awaria.objects.filter(status="W toku")
        else:
            if wybranaMaszyna != "":
                dane = Awaria.objects.filter(
                    status="W toku", maszyna=wybranaMaszyna)
            if wybranyZgłaszający != "":
                dane = Awaria.objects.filter(
                    status="W toku", zgłaszający=wybranyZgłaszający)
            if wybranyAlert != "":
                dane = Awaria.objects.filter(
                    status="W toku", stopień_alertu=wybranyAlert)
        if form.is_valid():
            pass
    else:
        form = Filtrowanie()
    context = {
        'form': form,
        'dane': dane
    }
    return render(request, 'rejestrAwarii/wToku.html', context)


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


def zakonczone(request):
    wpisy = Awaria.objects.filter(status="Zakończone")
    return render(request, 'rejestrAwarii/zakończone.html', {'wpisy': wpisy})
