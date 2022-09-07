from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.places'
    verbose_name= "Место"
    verbose_name_plural= "Места"
