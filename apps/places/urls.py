from django.urls import path 
from apps.places.views import places

urlpatterns = [
    path('places/all', places, name = "places"),
   
]