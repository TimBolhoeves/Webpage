# Generated by Django 4.1 on 2022-08-16 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_alter_users_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='image',
        ),
    ]
