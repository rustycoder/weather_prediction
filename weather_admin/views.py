from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from weather_prediction.settings import EMAIL_HOST_USER

# from .service.OpenWeatherServiceImpl import current_weather_data
from .service.OpenWeatherService import OpenWeatherService
from .forms import SignUpForm
from .models import Profile
from datetime import datetime


def admin_home(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(username=request.user)
        current_profile = Profile.objects.get(user=current_user)
        # TODO Get Open API Realtime Data
        open_weather_service = OpenWeatherService()
        weather_data, error_message = open_weather_service.current_weather_data(27.7172, 85.3240)
        if weather_data:
            print(weather_data)
            print(type(weather_data))
        elif error_message:
            print(f"Error: {error_message}")
        else:
            print("An unknown error occurred.")
        return render(request, 'home.html', {'current_user':current_user, 'current_profile':current_profile, 'weather_data':weather_data})
    else:
        return render(request, 'login.html', {})



def admin_login(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return redirect('weather_admin_home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in.")
                return redirect('weather_admin_home')
            else:
                messages.success(request, "There was an error. Please, try again.")
                return render(request, 'login.html', {})
        else:
            return render(request, 'login.html', {})



def admin_register(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return redirect('weather_admin_home')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                # Authenticate and login
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "You Have Successfully Registered! Welcome!")
                return redirect('weather_admin_home')
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})



def admin_logout(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect('weather_admin_login')



def admin_forgot_password(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return redirect('weather_admin_home')
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
        return redirect('weather_admin_home')
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