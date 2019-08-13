# Generated by Django 2.1 on 2019-08-09 06:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20190809_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='finalExam',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Examen Final'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='finalGrade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2, verbose_name='Promedio Final'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='midTerm',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Intermedio'),
        ),
    ]