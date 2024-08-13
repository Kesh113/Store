from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Products, Category

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ['product_name', 'slug', 'photo', 'post_photo', 'description', 'characters', 'price', 'count', 'is_published', 'category', 'order_quantity', 'rating', 'comment_quantity']
    prepopulated_fields = {"slug": ["product_name"]}
    readonly_fields = ['post_photo']
    list_editable = ['is_published']
    list_per_page = 15
    search_fields = ['product_name', 'category']
    actions = ['set_published', 'set_hidden']
    list_filter = ['product_name', 'category', 'price', 'count', 'is_published', 'order_quantity', 'rating', 'comment_quantity']
    list_display = ['product_name', 'category', 'price', 'count', 'is_published', 'order_quantity', 'rating', 'comment_quantity', 'post_photo']
    list_display_links = ['product_name']
    
    @admin.display(description="Изображение", ordering='content')
    def post_photo(self, products: Products):
        if products.photo:
            return mark_safe(f"<img src='{products.photo.url}' width=150>")
        return "Без фото"
    
    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Products.Status.PUBLISHED)
        self.message_user(request, f"Опубликовано {count} записей.")

    @admin.action(description='Скрыть выбранные записи')
    def set_hidden(self, request, queryset):
        count = queryset.update(is_published=Products.Status.HIDDEN)
        self.message_user(request, f"Скрыто {count} записей.", messages.WARNING)
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["cat_name"]}
    list_display = ['id', 'cat_name']
    list_display_links = ['cat_name']
