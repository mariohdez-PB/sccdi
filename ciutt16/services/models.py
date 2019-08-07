from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator, MinValueValidator 

def custom_upload_to(instance, filename):
    old_instance = Service.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'services/' + filename

def custom_attendance_upload_to(instance, filename):
    old_instance = Post.objects.get(pk=instance.pk)
    old_instance.attendance.delete()
    return 'attendance/' + filename

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to=custom_upload_to, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "idioma"
        verbose_name_plural = "idiomas"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    schedule = models.TextField(verbose_name="Horario")
    place = models.CharField(max_length=200, verbose_name="Edificio")
    classroom = models.CharField(max_length=200, verbose_name="Aula")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    attendance = models.FileField(verbose_name="Asistencias", upload_to=custom_attendance_upload_to, null=True, blank=True)
    status = models.CharField(max_length=200, verbose_name="Estatus")
    course = models.ForeignKey(Service, verbose_name="Curso", on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, verbose_name="Profesor", on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Inscription(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Post, on_delete=models.CASCADE)
    fstGrade = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name="Parcial 1", default=0)
    sndGrade = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name="Parcial 2", default=0)
    trdGrade = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name="Parcial 3", default=0)
    fthGrade = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name="Parcial 4", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de inscripción")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "inscripcion"
        verbose_name_plural = "inscripciones"
        ordering = ['-created']

    def __str__(self):
        return self.student,self.course