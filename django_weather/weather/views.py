from django.shortcuts import render, redirect
from .forms import WeatherForm
from .weather_api_service import get_weather_json_with_all_info_in_city



def index(request):
    context = {}
    form = WeatherForm()
    context['form'] = form
    if request.method == 'POST':
            city_name = request.POST.get('city')
            language_code = request.POST.get('language_choice')
            weather_json = get_weather_json_with_all_info_in_city(city_name=city_name, language_code=language_code)
            if (weather_json['success']):
                context.update({'city_weather': weather_json, 'weather_error': False})
            else:
                context.update({'weather_error': True})
    return render(request, 'weather/index.html', context)


def weather_newsletter(request):
    context = {}
    return render(request, 'weather/newsletter.html', context)