# Generated by Django 2.1 on 2019-08-04 08:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import services.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fstGrade', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Parcial 1')),
                ('sndGrade', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Parcial 2')),
                ('trdGrade', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Parcial 3')),
                ('fthGrade', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Parcial 4')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de inscripción')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'inscripcion',
                'verbose_name_plural': 'inscripciones',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('schedule', models.TextField(verbose_name='Horario')),
                ('classroom', models.CharField(max_length=200, verbose_name='Aula')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('attendance', models.FileField(blank=True, null=True, upload_to=services.models.custom_attendance_upload_to, verbose_name='Asistencias')),
                ('status', models.CharField(max_length=200, verbose_name='Estatus')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'idioma', 'verbose_name_plural': 'idiomas'},
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=services.models.custom_upload_to, verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='post',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service', verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='post',
            name='teacher',
            field=models.ManyToManyField(related_name='get_posts', to=settings.AUTH_USER_MODEL, verbose_name='Profesor'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Post'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]