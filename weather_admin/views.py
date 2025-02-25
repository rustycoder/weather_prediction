from django.template import loader
from django.http import HttpResponse


# Create your views here.
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def forgot_password(request):
    template = loader.get_template('forgot_password.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())