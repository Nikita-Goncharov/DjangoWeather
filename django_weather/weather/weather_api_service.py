import requests 
from typing import Optional
from django.conf import settings

api_key = settings.API_KEY
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_current_weather_json_in_city(city_name: str, language_code: str) -> dict:
    complete_url = f'{base_url}appid={api_key}&q={city_name}&lang={language_code}'
    try:
        response = requests.get(complete_url).json()
    except: 
        return {'success': False}

    icon_url = _get_weather_icon_for_display_on_page(response['weather'][0]['icon'])
    response.update({'success': True, 'icon_url': icon_url})
    return response


def _get_weather_icon_for_display_on_page(icon_code: str) -> str:
    icon_url = f"http://openweathermap.org/img/w/{icon_code}.png"
    return icon_url
