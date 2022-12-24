from django.shortcuts import render, redirect
from .forms import WeatherForm
from .weather_api_service import get_current_weather_json_in_city

def index(request):
    context = {}
    form = WeatherForm()
    context['form'] = form
    if request.method == 'POST':
            city_name = request.POST.get('city')
            language_code = request.POST.get('language_choice')
            response = get_current_weather_json_in_city(city_name=city_name, language_code=language_code)
            context.update(response)
    return render(request, 'weather/index.html', context)


def weather_newsletter(request):
    context = {}
    return render(request, 'weather/newsletter.html', context)