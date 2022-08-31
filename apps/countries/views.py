from django.shortcuts import render, redirect
from apps.countries.models import Country, CountryImage
from apps.settings.models import Setting

# Create your views here.
def country(request):
    country = Country.objects.all()
    context = {
        'countries' : country,
    }
    return render(request, 'index.html', context)

def add_country(request):
    setting= Setting.objects.latest('id')
    if request.method == "POST":
        title= request.POST.get("title")
        description= request.POST.get("description")
        image= request.FILES.get("image")
        counrty= Country.objects.create(title= title, description=description, image= image)
        for p_image in image:
            CountryImage.objects.create(country_id = country.id, image = p_image)
        return redirect('counry')
    context={
        'setting': setting,
    }
    return render(request, 'country/create.html', context)
