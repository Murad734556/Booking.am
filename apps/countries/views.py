from django.shortcuts import render, redirect
from apps.countries.models import Country
from apps.settings.models import Setting
from apps.hotels.models import Hotel
from apps.places.models import Places

# Create your views here.


def country_detail(request, id):
    setting= Setting.objects.latest('id')
    countries= Country.objects.get(id=id)
    places= Places.objects.all().order_by('?')
    hotels= Hotel.objects.all().order_by('?')
    context={
        'setting': setting,
        'countries': countries,
        'hotels': hotels,
        'places': places
        }
    return render(request ,'country/countries_detail.html', context)

def countries(request):
    setting= Setting.objects.latest('id')
    countries= Country.objects.all().order_by('?')
    context= {
        'setting': setting,
        'countries': countries
    }

    return render(request, 'country/countries.html', context)


