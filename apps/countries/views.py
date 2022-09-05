from django.shortcuts import render, redirect
from apps.countries.models import Country, CountryImage
from apps.settings.models import Setting
from apps.hotels.models import Hotel

# Create your views here.


def country_detail(request, id):
    setting= Setting.objects.latest('id')
    countries= Country.objects.get(id=id)
    hotels= Hotel.objects.all().order_by('?')
    context={
        'setting': setting,
        'countries': countries,
        'hotels': hotels
        }
    return render(request ,'country/countries_detail.html', context)



