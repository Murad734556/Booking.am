from django.urls import path 
from apps.countries.views import country

urlpatterns = [
path('country/', country, name="country")

]