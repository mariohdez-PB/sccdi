from django.db import models
from ckeditor.fields import RichTextField

def custom_upload_to(instance, filename):
    old_instance = Page.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'pages/' + filename

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    image = models.ImageField(verbose_name="Imagen", upload_to=custom_upload_to, null=True, blank=True)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title