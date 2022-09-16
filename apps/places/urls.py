from django.urls import path 
from apps.places.views import place_detail

urlpatterns = [
    path('place/<int:id>', place_detail, name="place_detail")
]