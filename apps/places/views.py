from django.shortcuts import render
from apps.countries.models import Country
from apps.settings.models import Setting
from apps.places.models import Places
# Create your views here.

def place_detail(request, id):
    setting = Setting.objects.latest('id')
    places = Places.objects.get(id=id)
    context ={
        'setting': setting,
        'places': places,
    }

    return render(request, 'places/place_detail.html', context)