import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = '44226adae6d661b8727fde745007f83c'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    

    if(request.method == 'POST'):
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
            'pressure': res["main"]["pressure"],
            'wind': res["wind"]["speed"],
            'icon': res["weather"][0]['icon']
        }
        all_cities.append(city_info)

        all_cities = all_cities[-3:]

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
