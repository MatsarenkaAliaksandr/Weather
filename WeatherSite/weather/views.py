from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = '6c1940ed9b997a5c1e753a24acd15b76'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


def mytemplate(request):
    appid = '6c1940ed9b997a5c1e753a24acd15b76'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'description': res['weather'][0]['description'],
            'feels_like': res["main"]["feels_like"],
            'pressure': res["main"]["pressure"],
            'wind': res["wind"]["speed"],
            'icon': res["weather"][0]["icon"],
        }
        all_cities.insert(0,city_info)

    context = {'all_info': all_cities,'form': form}
    return render(request, 'weather/mytemplate.html', context)
