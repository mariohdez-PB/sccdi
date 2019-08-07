from django.contrib import admin
from .models import Service, Post, Inscription

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class InscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Inscription, InscriptionAdmin)