# Generated by Django 4.1 on 2022-08-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='Niet ingevuld', max_length=255, unique=True),
        ),
    ]
