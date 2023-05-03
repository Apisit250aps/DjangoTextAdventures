from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def is_authenticated(request):
    try :
        return '_auth_user_id' in request.session
    except :
        return False

def index(req):

    if User.objects.filter(username='admin'):
        print("Admin")
    else:
        try:
            User.objects.create_superuser(
                username='admin',
                password='admin',
                email="admin001@gmail.com")

            print("created!")
        except:
            print("error")

    return redirect("gate_page")


def Gate(req):
    return render(req, 'gate/gate.html')


def Login(request):

    try:
        for i, o in request.session.items():
            print(i, o)
    except:
        pass

    if is_authenticated(request):
        return redirect("gate_page")
    

    return render(request, 'gate/login.html')


def Register(req):
    if is_authenticated(req):
        return redirect("gate_page")
    
    return render(req, 'gate/register.html')


def Menu(req):
    return render(req, 'gate/menu.html')
