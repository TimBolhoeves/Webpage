# Generated by Django 4.1 on 2022-08-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='./static/images'),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(upload_to='./static/images'),
        ),
    ]
