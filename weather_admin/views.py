from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def admin_home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return render(request, 'login.html', {})

def admin_login(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return render(request, 'home.html', {})
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in.")
                return render(request, 'home.html', {})
            else:
                messages.success(request, "There was an error. Please, try again.")
                return redirect('weather_admin_login')
        else:
            return render(request, 'login.html', {})

def admin_forgot_password(request):
    template = loader.get_template('forgot_password.html')
    return HttpResponse(template.render())

def admin_register(request):
    if request.user.is_authenticated:
        messages.success(request, "You have been logged in.")
        return redirect('weather_admin_home')
    else:
        return render(request, 'register.html', {})

def admin_logout(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect('weather_admin_home')