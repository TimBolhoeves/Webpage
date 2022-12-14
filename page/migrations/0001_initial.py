# Generated by Django 4.1 on 2022-08-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Niet ingevuld', max_length=255)),
                ('price', models.CharField(default='Niet ingevuld', max_length=255)),
                ('stock', models.CharField(default='Niet ingevuld', max_length=255)),
                ('image', models.ImageField(upload_to='./page/static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Niet ingevuld', max_length=255)),
                ('password', models.CharField(default='Niet ingevuld', max_length=255)),
                ('rank', models.CharField(default='Niet ingevuld', max_length=255)),
                ('image', models.ImageField(upload_to='./page/static/images')),
            ],
        ),
    ]
