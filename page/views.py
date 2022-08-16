from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Users, Item
from datetime import date, datetime
from django.views.csrf import *

def index(request):
    item = Item.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())