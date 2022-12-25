import requests 
from django.conf import settings

api_key = settings.API_KEY
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather_json_with_all_info_in_city(city_name: str, language_code: str) -> dict:
    complete_url = f'{base_url}appid={api_key}&q={city_name}&lang={language_code}'
    
    try: 
        response = requests.get(complete_url).json()
        icon_url = _get_weather_icon_for_display_on_page(response['weather'][0]['icon'])
    except:
        return {'success': False}
    necessary_weather_info = _get_necessary_weather_info(response)
    necessary_weather_info.update({'success': True, 'icon_url': icon_url})

    return necessary_weather_info


# Response example
"""
{
  "coord": {
    "lon": 10.99,
    "lat": 44.34
  },
  "weather": [
    {
      "id": 501,
      "main": "Rain",
      "description": "moderate rain",
      "icon": "10d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 298.48,
    "feels_like": 298.74,
    "temp_min": 297.56,
    "temp_max": 300.05,
    "pressure": 1015,
    "humidity": 64,
    "sea_level": 1015,
    "grnd_level": 933
  },
  "visibility": 10000,
  "wind": {
    "speed": 0.62,
    "deg": 349,
    "gust": 1.18
  },
  "rain": {
    "1h": 3.16
  },
  "clouds": {
    "all": 100
  },
  "dt": 1661870592,
  "sys": {
    "type": 2,
    "id": 2075663,
    "country": "IT",
    "sunrise": 1661834187,
    "sunset": 1661882248
  },
  "timezone": 7200,
  "id": 3163858,
  "name": "Zocca",
  "cod": 200
}
"""


def _get_weather_icon_for_display_on_page(icon_code: str) -> str:
    icon_url = f"http://openweathermap.org/img/w/{icon_code}.png"
    return icon_url


def _get_necessary_weather_info(weather_json:str) -> dict:
    necessary_info = {
        'weather_name': weather_json['weather'][0]['main'],
        'weather_description': weather_json['weather'][0]['description'].capitalize(),
        'temp': weather_json['main']['temp'],
        'temp_feels_like': weather_json['main']['feels_like'],
        'wind_speed': weather_json['wind']['speed'],  
    }
    return necessary_info

