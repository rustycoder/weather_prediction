from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from weather_prediction.settings import EMAIL_HOST_USER

from .service.OpenWeatherService import OpenWeatherService
from .forms import SignUpForm, ProfileForm
from .models import Profile

from loguru import logger

import random


def admin_dashboard(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(username=request.user)
        current_profile = Profile.objects.get(user=current_user)

        open_weather_service = OpenWeatherService()
        weather_data, error_message = open_weather_service.current_weather_data(27.7172, 85.3240)
        logger.debug(weather_data)
        return render(request, 'dashboard.html', {'current_user':current_user, 'current_profile':current_profile, 'weather_data':weather_data})
    else:
        return render(request, 'login.html', {})



def profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(username=request.user)
        current_profile = Profile.objects.get(user=current_user)
        return render(request, 'profile.html', {'current_user':current_user, 'current_profile':current_profile})
    else:
        return render(request, 'login.html', {})



def weather_realtime(request):
    if request.user.is_authenticated:
        open_weather_service = OpenWeatherService()
        weather_data, error_message = open_weather_service.current_weather_data(27.7172, 85.3240)
        logger.debug(weather_data)
        return render(request, 'weather_realtime.html', {'weather_data':weather_data})
    else:
        return render(request, 'login.html', {})



def air_pollution_realtime(request):
    if request.user.is_authenticated:
        open_weather_service = OpenWeatherService()
        air_pollution_data, error_message = open_weather_service.current_air_pollution_data(27.7172, 85.3240)
        logger.debug(air_pollution_data)
        return render(request, 'air_pollution_realtime.html', {'air_pollution_data':air_pollution_data})
    else:
        return render(request, 'login.html', {})
    


def weather_forecast(request):
    if request.user.is_authenticated:
        open_weather_service = OpenWeatherService()
        weather_forecast, error_message = open_weather_service.five_day_weather_forecast(27.7172, 85.3240)
        logger.debug(weather_forecast)
        return render(request, 'weather_forecast.html', {'weather_forecast':weather_forecast})
    else:
        return render(request, 'login.html', {})



def air_pollution_forecast(request):
    if request.user.is_authenticated:
        open_weather_service = OpenWeatherService()
        air_pollution_forecast, error_message = open_weather_service.forecast_air_pollution_data(27.7172, 85.3240)
        logger.debug(air_pollution_forecast)
        return render(request, 'air_pollution_forecast.html', {'air_pollution_forecast':air_pollution_forecast})
    else:
        return render(request, 'login.html', {})



def weather_prediction(request):
    if request.user.is_authenticated:
        return render(request, 'weather_prediction.html', {})
    else:
        return render(request, 'login.html', {})



def admin_login(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return redirect('weather_admin_dashboard')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in.")
                return redirect('weather_admin_dashboard')
            else:
                messages.success(request, "There was an error. Please, try again.")
                return render(request, 'login.html', {})
        else:
            return render(request, 'login.html', {})



def admin_register(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return redirect('weather_admin_dashboard')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                # Authenticate and login
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                logger.debug(user)
                login(request, user)
                current_user = User.objects.get(username=user)
                current_profile = Profile()
                logger.debug(current_profile)
                current_profile.otp = random.randint(1000000, 9999999)
                current_profile.user = current_user
                current_profile.save()
                messages.success(request, "You Have Successfully Registered! Welcome!")
                return redirect('weather_admin_dashboard')
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})



def profile_update(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(username=request.user)
        current_profile = Profile.objects.get(user=current_user)
        if request.method == 'GET':
            form = ProfileForm(instance=current_profile)
            return render(request, 'profile_update.html', {'form':form})
        elif request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                current_profile.phone = form.cleaned_data['phone']
                current_profile.address = form.cleaned_data['address']
                current_profile.city = form.cleaned_data['city']
                current_profile.state = form.cleaned_data['state']
                current_profile.zipcode = form.cleaned_data['zipcode']
                current_profile.save()
                messages.success(request, "You Have Successfully Updated Your Profile.")
                return redirect('weather_admin_profile')
            else:
                return render(request, 'profile_update.html', {'form':form})
    else:
        return render(request, 'login.html', {})



def admin_logout(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect('weather_admin_login')



def admin_forgot_password(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return redirect('weather_admin_dashboard')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            if User.objects.filter(email=email).exists():
                # TODO Send Email
                user = User.objects.get(email=email)
                profile = Profile.objects.get(user=user)
                send_mail(
                    "Reset your password : Weather Prediction Application",
                    f"Hey {user}, want to reset password. Click on the link http://127.0.0.1:8000/weather_admin/reset_password?username={user}&otp={profile.otp}",
                    EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, f"Reset password link has been sent to your {email}.")
                return render(request, 'forgot_password.html', {})
            else:
                messages.success(request, f"{email} does not exist.")
                return render(request, 'forgot_password.html', {})
        else:
            return render(request, 'forgot_password.html', {})



def admin_reset_password(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return redirect('weather_admin_dashboard')
    else:
        if request.method == 'GET':
            username = request.GET['username']
            otp = request.GET['otp']
            return render(request, 'reset_password.html', {'username':username, 'otp':otp})
        elif request.method == 'POST':
            username = request.POST['username']
            otp = request.POST['otp']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    db_user = User.objects.get(username=username)
                    db_profile = Profile.objects.get(user=db_user)
                    if db_profile.otp == otp:
                        db_user.set_password(password1)
                        db_user.save()
                        messages.success(request, f"Password has been reset. Try to login with new password")
                        return redirect('weather_admin_login')
                    else:
                        messages.success(request, f"Password do not match. Try again")
                        return render(request, 'reset_password.html', {'username':username, 'otp':otp})
            else:
                messages.success(request, f"Password do not match. Try again")
                return render(request, 'reset_password.html', {'username':username, 'otp':otp})
        else:
            return redirect('weather_admin_login')