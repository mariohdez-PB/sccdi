# Generated by Django 2.1 on 2019-08-09 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_auto_20190809_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='finalGrade',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Promedio Final'),
        ),
    ]
