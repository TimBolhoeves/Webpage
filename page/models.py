from django.db import models
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=255, default='Niet ingevuld')
    description = models.CharField(max_length=255, default='Niet ingevuld')
    price = models.CharField(max_length=255, default='Niet ingevuld')
    type = models.CharField(max_length=255, default='Niet ingevuld')
    stock = models.CharField(max_length=255, default='0')
    image = models.ImageField(upload_to='./static/images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
