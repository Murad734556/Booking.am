from django.shortcuts import render, redirect
from apps.settings.models import Setting, Contact
from apps.countries.models import Country
from apps.places.models import Places
from apps.hotels.models import Hotel

from django.db.models import Q
# Create your views here.


def index(request):
    setting= Setting.objects.latest('id')
    countries = Country.objects.all().order_by('?')
    hotels= Hotel.objects.all().order_by('?')
    places = Places.objects.all().order_by('?')
    context={
        'setting': setting,
        'countries': countries,
        'hotels': hotels,
        'places': places,
    }
    return render(request, 'index.html', context)



def about(request):
    setting = Setting.objects.latest('id')
    context={
        'setting': setting,
    }
    return render(request, 'about.html', context)

def find_place(request):
    setting = Setting.objects.latest('id')
    # places= Places.objects.all()
    qury_object= request.GET.get('key')
    if qury_object:
        places = Places.objects.filter(Q(title__icontains = qury_object) | Q(description__icontains = qury_object))
    context ={
        'setting': setting,
        'places': places,
            }
    return render(request, 'booking.html', context)

def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        email = request.POST.get('email')
        title = request.POST.get('title')
        phone = request.POST.get('phone')
        problem = request.POST.get('problem')
        contact = Contact.objects.create(user = request.user, email = email, title = title, phone = phone, problem = problem)
        return redirect('index')
    context = {
        'setting' : setting,
    }
    return render(request, 'contact.html', context)

