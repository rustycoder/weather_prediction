from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='weather_admin_dashboard'),
    path('search', views.admin_search, name='weather_admin_search'),
    path('login', views.admin_login, name='weather_admin_login'),
    path('register', views.admin_register, name='weather_admin_register'),
    path('logout', views.admin_logout, name='weather_admin_logout'),
    path('forgot_password', views.admin_forgot_password, name='weather_admin_forgot_password'),
    path('reset_password', views.admin_reset_password, name='weather_admin_reset_password'),

    path('profile', views.profile, name='weather_admin_profile'),
    path('update_profile', views.profile_update, name='weather_admin_profile_update'),

    path('weather_realtime', views.weather_realtime, name='weather_admin_weather_realtime'),
    path('weather_forecast', views.weather_forecast, name='weather_admin_weather_forecast'),
    path('weather_prediction', views.weather_prediction, name='weather_admin_weather_prediction'),
    
    path('air_pollution_realtime', views.air_pollution_realtime, name='weather_admin_air_pollution_realtime'),
    path('air_pollution_forecast', views.air_pollution_forecast, name='weather_admin_air_pollution_forecast'),

    path('api/v1/weather_overview', views.api_weather_overview, name='api_weather_realtime'),

]