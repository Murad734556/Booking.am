from django.contrib import admin
from apps.countries.models import Country, CountryImage
# Register your models here.


admin.site.register(Country)
admin.site.register(CountryImage)