from django import template
from services.models import Inscription

register = template.Library()

@register.simple_tag
def get_inscription_list():
    inscriptions = Inscription.objects.all()
    return inscriptions