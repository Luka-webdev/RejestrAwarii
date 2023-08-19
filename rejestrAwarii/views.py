from django.shortcuts import render


def welcomeScreen(request):
    return render(request, 'rejestrAwarii/welcomeScreen.html', {})
