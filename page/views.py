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
from .forms import ItemForm
from django.contrib.auth.decorators import login_required, permission_required
import os

today = datetime.now()
today_format = today.strftime('%Y-%m-%d')

# home page
def index(request):
    item = Item.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'item': item,
        'today': today,
    }
    return HttpResponse(template.render(context, request))

#------------------------------------------------------------
# CRUD operations --->

# page for adding items
@login_required
@permission_required('page.add_item', raise_exception=True)
def additem(request):
    context = {}
    context['form'] = ItemForm()
    return render( request, "additem.html", context)

# adds items using form params
@login_required
@permission_required('page.add_item', raise_exception=True)
def add(request):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    type = request.POST['type']
    stock = request.POST['stock']
    image = request.FILES['image']
    obj = Item(name=name, description=description, price=price, type=type, stock=stock, image=image)
    obj.save()
    return HttpResponseRedirect(reverse('index'))

# This function auto deletes the related image saved in media/images by using django-cleanup (https://pypi.org/project/django-cleanup/)
@login_required
@permission_required('page.delete_item', raise_exception=True)
def deleteitem(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    messages.info(request, 'Succesfully deleted the item')
    return HttpResponseRedirect(reverse('index'))

# page of item updates (except images)
@login_required
@permission_required('page.change_item', raise_exception=True)
def updateitem(request, id):
    item = Item.objects.get(id=id)
    template = loader.get_template('updateitem.html')
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context, request))

# updates everything except the image
@login_required
@permission_required('page.change_item', raise_exception=True)
def update(request, id):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    type = request.POST['type']
    stock = request.POST['stock']

    updateditem = Item.objects.get(id=id)

    updateditem.name = name
    updateditem.description = description
    updateditem.price = price
    updateditem.type = type
    updateditem.stock = stock
    updateditem.save()
    return HttpResponseRedirect(reverse('index'))

# page that only updates the image of an item
@login_required
@permission_required('page.change_item', raise_exception=True)
def updateimage(request, id):
    item = Item.objects.get(id=id)
    template = loader.get_template('updateimage.html')
    context = {
        'item': item,
    }
    return HttpResponse(template.render(context, request))

# updates only the image of an item
@login_required
@permission_required('page.change_item', raise_exception=True)
def updateimg(request, id):
    image = request.FILES['image']
    updateditem = Item.objects.get(id=id)
    updateditem.image = image
    updateditem.save()
    return HttpResponseRedirect(reverse('index'))

# <--- CRUD operations
#------------------------------------------------------------

#------------------------------------------------------------
# user authentication --->

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

# <--- user authentication
#------------------------------------------------------------