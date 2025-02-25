from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='weather_admin_login'),
    path('forgot_password', views.forgot_password, name='weather_admin_forgot_password'),
    path('register', views.register, name='weather_admin_register'),
    path('dashboard', views.dashboard, name='weather_admin_dashboard'),
]