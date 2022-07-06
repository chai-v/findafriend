from pickle import TRUE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import profile
from django.urls import reverse

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

#Checks username and password to login
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']

        names = list(profile.objects.values_list('name', flat=True))
        passes = list(profile.objects.values_list('password', flat=True))

        if uname in names:
            index = names.index(uname)
            if passw == passes[index]:
                return render(request, 'browse.html')
            else:
                return redirect(reverse('login'))
        else:
            return redirect(reverse('login'))
    else:
         return render(request, 'login.html')

#User signup
def signup(request):
    if request.method == 'POST':
        uname = request.POST['name']
        passw = request.POST['pass']
        desc = request.POST['des']
        interest = request.POST['interest']
        c = request.POST['color']
        h = request.POST['hobby']
        f = request.POST['food']
        a = request.POST['age']

        names = list(profile.objects.values_list('name', flat=True))
        passes = list(profile.objects.values_list('password', flat=True))

        if uname in names and passw in passes:
            messages.info(request, "USER ALREADY EXISTS. LOGIN INSTEAD.")
            return render(request, 'signup.html')
        else:
            newprofile = profile(name = uname, password=passw, description = desc, interests = interest,
            color = c, hobby = h, food = f, age = a)
            newprofile.save()
            return render(request, 'browse.html')
    else:
        return render(request, 'signup.html')

def browse(request):
    profiles = profile.objects.all()
    return render(request, 'browse.html', {'profiles': profiles})

