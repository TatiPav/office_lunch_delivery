# Generated by Django 3.0.7 on 2020-06-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость, руб.'),
        ),
    ]