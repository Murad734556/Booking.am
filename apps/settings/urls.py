from django.urls import path
from apps.settings.views import index, about, find_place, contact


urlpatterns = [
    path('', index, name = "index"),
    path('about/<int:id', about, name="about"),
    path('booking/', find_place, name="find_place"),
    path('contact/', contact, name="contact")
]