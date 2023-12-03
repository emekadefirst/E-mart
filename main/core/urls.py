from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('detail', views.detail, name='detail'),
    path('history', views.history, name='history'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]
