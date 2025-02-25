from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name='weather_admin_home'),
    path('login', views.admin_login, name='weather_admin_login'),
    path('forgot_password', views.admin_forgot_password, name='weather_admin_forgot_password'),
    path('register', views.admin_register, name='weather_admin_register'),
    path('logout', views.admin_logout, name='weather_admin_logout'),
]