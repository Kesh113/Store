from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Products, Category
from products.utils import DataMixin


class ProductsHome(DataMixin, ListView):
    context_object_name = 'products'
    template_name = 'products/index.html'
    title_page = 'Магазин товаров'
    cat_selected = 0
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.all()
        
        return context
    
    def get_queryset(self):
        return cache.get_or_set('products_categories', Products.published.all().select_related('category'), 60)
        

def products_cart(request):
    return render(request, 'products/cart.html')

def products_login(request):
    return render(request, 'products/login.html')

def products_about(request):
    return render(request, 'products/about.html')