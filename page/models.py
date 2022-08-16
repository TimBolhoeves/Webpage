from django.db import models
from django.urls import reverse

class Users(models.Model):
    name = models.CharField(max_length=255, default='Niet ingevuld')
    password = models.CharField(max_length=255, default='Niet ingevuld')
    rank = models.CharField(max_length=1, default='3')
    image = models.ImageField(upload_to='./page/static/images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("users_detail", kwargs={"pk": self.pk})
        

class Item(models.Model):
    name = models.CharField(max_length=255, default='Niet ingevuld')
    price = models.CharField(max_length=255, default='Niet ingevuld')
    stock = models.CharField(max_length=255, default='0')
    image = models.ImageField(upload_to='./page/static/images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
