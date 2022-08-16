from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Users, Item
from datetime import date, datetime
from django.views.csrf import *

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())