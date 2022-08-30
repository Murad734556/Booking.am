from django.apps import AppConfig


class CountriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.countries'
    verbose_name="Страна"
    verbose_name_plural="Страны"