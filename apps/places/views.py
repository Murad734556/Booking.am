from django.shortcuts import render
from apps.settings.models import Setting
from apps.places.models import Places
# Create your views here.

def hotel_detail(request, id):
    setting= Setting.objects.latest('id')
    places= Places.objects.get(id=id)
    context={
        'setting': setting,
        'places': places,
    }
    return render(request, 'places/place_detail.html', context )

def places(request):
    setting= Setting.objects.latest('id')
    places= Places.objects.all().order_by('?')
    context={
        'setting': setting,
        'places': places,
    }

    return render(request, 'places/places.html', context)