from pickle import TRUE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import profile
from django.urls import reverse
from django.http import Http404

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
                return redirect('browse')
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
            return redirect('browse')
    else:
        return render(request, 'signup.html')

def browse(request):
    if request.method == 'POST':
        fr = request.POST['fname']
        sort = request.POST['sort']
        
        if fr!="":
            values = fr.split(":")
            value = values[1]
            column = values[0]
        

        sortvalues = {
            "Alphabetic Ascending": 'name',
            "Alphabetic Descending": '-name',
            "Age Ascending": 'age',
            "Age Descending": '-age',
        }

        if fr!="" and sort!="select":
            values = list(profile.objects.values_list(column, flat=True))
            if value in values:
                if column=="color":
                    prof = profile.objects.filter(color = value).values()
                    sortvalue = sortvalues[sort]
                    prof = prof.order_by(sortvalue).values()
                    return render(request, 'browse.html', {'profiles':prof})
                elif column=="hobby":
                    prof = profile.objects.filter(hobby = value).values()
                    sortvalue = sortvalues[sort]
                    prof = prof.order_by(sortvalue).values()
                    return render(request, 'browse.html', {'profiles':prof})
                elif column=="food":
                    prof = profile.objects.filter(food = value).values()
                    sortvalue = sortvalues[sort]
                    prof = prof.order_by(sortvalue).values()
                    return render(request, 'browse.html', {'profiles':prof})
                else:
                    return redirect(reverse('browse'))

        elif fr!="":
            values = list(profile.objects.values_list(column, flat=True))
            if value in values:
                if column=="color":
                    prof = profile.objects.filter(color = value).values()
                    return render(request, 'browse.html', {'profiles':prof})
                elif column=="hobby":
                    prof = profile.objects.filter(hobby = value).values()
                    return render(request, 'browse.html', {'profiles':prof})
                elif column=="food":
                    prof = profile.objects.filter(food = value).values()
                    return render(request, 'browse.html', {'profiles':prof})
        elif sort!="select":
            sortvalue = sortvalues[sort]
            prof = profile.objects.all().order_by(sortvalue).values()
            return render(request, 'browse.html', {'profiles':prof})
        else:
            return redirect(reverse('browse')) 
    else:
        profiles = profile.objects.all()
        return render(request, 'browse.html', {'profiles':profiles})