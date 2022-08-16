from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Item
from datetime import date, datetime
from django.views.csrf import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth

def index(request):
    item = Item.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    return render(request, 'login.html', {})

def loginpost(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Succesfully logged out')
    return redirect('index')