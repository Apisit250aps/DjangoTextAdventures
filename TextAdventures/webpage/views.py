from django.shortcuts import render, redirect

# Create your views here.


def index(req):
    return redirect("gate_page")


def Gate(req):
    return render(req, 'gate/gate.html')


def Login(req):
    return render(req, 'gate/login.html')


def Register(req):
    return render(req, 'gate/register.html')


def Menu(req):
    return render(req, 'gate/menu.html')
