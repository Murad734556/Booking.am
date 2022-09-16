from django.shortcuts import render
from apps.settings.models import Setting
from apps.countries.models import Country
from apps.hotels.models import Hotel
from apps.places.models import Places

def hotel_detail(request, id):
    setting= Setting.objects.latest('id')
    hotels= Hotel.objects.get(id=id)
    context={
        'setting': setting,
        'hotels': hotels,
    }
    return render(request, 'hotels/hotel_detail.html', context )

def hotels(request, id):
    setting = Setting.objects.latest('id')
    places = Places.objects.get(id = id)
    hotels = Hotel.objects.all().order_by('?')
    context ={
        'setting': setting,
        'hotels': hotels,
        'places': places,
    }

    return render(request, 'hotels/hotels.html', context)
