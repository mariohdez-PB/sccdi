from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = 'services'
    verbose_name = "Gestor de Cursos"
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }