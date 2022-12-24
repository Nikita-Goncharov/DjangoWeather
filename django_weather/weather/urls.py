from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'), #IndexView.as_view()
    path('telegram_weatherletter/', views.weather_newsletter, name='newsletter')
]