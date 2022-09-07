from django.urls import path 
from apps.countries.views import country_detail, countries

urlpatterns = [
    path('country/<int:id>', country_detail, name="country_detail" ),
    path('countries/all', countries, name='countries')

]