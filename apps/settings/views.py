from django.shortcuts import render
from apps.settings.models import Setting
from apps.countries.models import Country
from apps.hotels.models import Hotel
# Create your views here.


def index(request):
    setting= Setting.objects.latest('id')
    countries = Country.objects.all().order_by('?')
    hotels= Hotel.objects.all().order_by('?')
    context={
        'setting': setting,
        'countries': countries,
        'hotels': hotels,
    }
    return render(request, 'index.html', context)



def about(request):
    setting = Setting.objects.latest('id')
    context={
        'setting': setting,
    }
    return render(request, 'about.html', context)
