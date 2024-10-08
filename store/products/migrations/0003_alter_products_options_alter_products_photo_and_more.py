# Generated by Django 5.0.7 on 2024-08-13 08:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['id'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(default='photos/13.08.2024/without_photo.jpg', upload_to='photos/%d.%m.%Y', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='products',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг'),
        ),
    ]
