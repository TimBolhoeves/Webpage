# Generated by Django 4.1 on 2022-08-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_item_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='Niet ingevuld', max_length=255),
        ),
    ]
