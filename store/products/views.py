from django.shortcuts import render

def products_home(request):
    return render(request, 'products/index.html', {'title': 'Магазин товаров'})

def products_cart(request):
    return render(request, 'products/cart.html')

def products_login(request):
    return render(request, 'products/login.html')

def products_about(request):
    return render(request, 'products/about.html')