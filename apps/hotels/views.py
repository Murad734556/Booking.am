from django.shortcuts import render
from apps.settings.models import Setting
from apps.countries.models import Country
from apps.hotels.models import Hotel

def hotel_detail(request, id):
    setting= Setting.objects.latest('id')
    hotels= Hotel.objects.get(id=id)
    context={
        'setting': setting,
        'hotels': hotels,
    }
    return render(request, 'hotels/hotel_detail.html', context )
