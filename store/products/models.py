from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Products.Status.PUBLISHED)

class Products(models.Model):
    
    class Status(models.IntegerChoices):
        HIDDEN = 0, 'Скрыто'
        PUBLISHED = 1, 'Опубликовано'
        
    product_name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, help_text='Слаг - это часть URL-адреса ресурса', verbose_name='Слаг')
    photo = models.ImageField(upload_to='photos/%d.%m.%Y', default='photos/13.08.2024/without_photo.jpg', verbose_name='Фото')
    description = models.TextField(default=None, blank=True, null=True, verbose_name='Описание')
    characters = models.TextField(default=None, blank=True, null=True, verbose_name='Характеристики')
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Цена')
    count = models.PositiveIntegerField(verbose_name='Количество')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.HIDDEN, verbose_name='Статус')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    order_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество заказов')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, verbose_name='Рейтинг')
    comment_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество опубликованных комментариев')
    
    objects = models.Manager()
    published = PublishedManager()
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['id']
    
class Category(models.Model):
    cat_name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, help_text='Слаг - это часть URL-адреса ресурса', verbose_name='Слаг категории')
    
    def __str__(self):
        return self.cat_name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
        
