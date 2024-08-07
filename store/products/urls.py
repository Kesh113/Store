from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.products_home, name='home'),
    path('cart/', views.products_cart, name='cart'),
    path('login/', views.products_login, name='login'),
    path('about/', views.products_about, name='about'),
]
