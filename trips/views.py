from django.shortcuts import render
from django.http import HttpResponse
from .data import CITIES, TIPS

def index(request):
    theme = request.COOKIES.get('theme', 'light')
    return render(request, 'trips/index.html', {
        'cities': CITIES,
        'tips': TIPS,
        'theme': theme
    })

def settings_view(request):
    theme = request.COOKIES.get('theme', 'light')
    currency = request.COOKIES.get('currency', 'USD')
    return render(request, 'trips/settings.html', {
        'theme': theme,
        'currency': currency
    })

def save_settings(request):
    if request.method == 'POST':
        theme = request.POST.get('theme', 'light')
        currency = request.POST.get('currency', 'USD')
        response = render(request, 'trips/saved.html')
        response.set_cookie('theme', theme, max_age=30*24*3600)
        response.set_cookie('currency', currency, max_age=30*24*3600)
        return response
    return HttpResponse("Ошибка")