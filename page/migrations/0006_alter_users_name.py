# Generated by Django 4.1 on 2022-08-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_alter_item_image_alter_users_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(default='Niet ingevuld', max_length=255, unique=True),
        ),
    ]
