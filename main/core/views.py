from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def detail(request):
    return render(request, 'detail.html')

def cart(request):
    return render(request, 'cart.html')

def history(request):
    return render(request, 'history.html')

