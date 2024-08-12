from django.contrib import admin

from .models import Products, Category

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ['product_name', 'slug', 'photo', 'description', 'characters', 'price', 'count', 'is_published', 'category']
    prepopulated_fields = {"slug": ["product_name"]}
    list_editable = ['is_published']
    list_per_page = 20
    search_fields = ['product_name', 'category']
    actions = ['set_published', 'set_hidden']
    list_filter = ['product_name', 'category', 'price', 'count', 'is_published']
    list_display = ['product_name', 'category', 'price', 'count', 'is_published']
    list_display_links = ['product_name']
    
    
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
