from django.contrib import admin
from apps.places.models import Places, PlaceImage
# Register your models here.


admin.site.register(Places)

admin.site.register(PlaceImage)