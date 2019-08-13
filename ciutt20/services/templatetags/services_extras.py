from django import template
from services.models import Service, Inscription, Group

register = template.Library()

@register.simple_tag
def get_service_list():
    services = Service.objects.all()
    return services
    
@register.simple_tag
def get_inscription_list():
    inscriptions = Inscription.objects.all()
    return inscriptions