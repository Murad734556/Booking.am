from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from apps.settings.models import Setting
from apps.users.models import User
from django.shortcuts import HttpResponse
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_image = request.FILES.get('profile_image')
        if password1 == password2:
        
                user = User.objects.create(first_name = first_name, last_name = last_name, email = email, phone = phone, username = username, profile_image = profile_image)
                user.set_password(password1)
                user.save()
                return redirect('user_login')
        else:
            return HttpResponse("Пароли не совпадают")

    context = {
        'setting' : setting,
    }
    return render(request, 'user/register.html', context)

def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return HttpResponse("Неправильные данные")

    context = {
        'setting' : setting,
    }
    return render(request, 'user/login.html', context)   


def profile(request, id):
    setting = Setting.objects.latest('id')
    user = User.objects.get(id = id)
    context = {
        'user' : user,
        'setting' : setting,
    }
    return render(request, 'user/profile.html', context)

def profile_update(request, id):
    setting = Setting.objects.latest('id')
    user = User.objects.get(id = id)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        profile_image = request.FILES.get('profile_image')
        phone = request.POST.get('phone')
        user = User.objects.get(id = id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username 
        user.email = email 
        user.profile_image = profile_image
        user.phone = phone 
        user.save()
        return redirect('profile', user.id)
    context = {
        'setting' : setting,
        'user' : user
    }
    return render(request, 'user/profile_update.html', context)

def profile_delete(request, id):
    context ={}
 
    obj = get_object_or_404(User, id = id)
    if request.method =="POST":

        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "user/delete.html", context)