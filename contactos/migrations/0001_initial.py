# Generated by Django 4.2.1 on 2023-06-12 21:15

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
                ('apellido', models.CharField(blank=True, max_length=50)),
                ('numero1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('numero2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('numero3', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('grupo', models.CharField(max_length=50)),
                ('fecha_inclusion', models.DateField(default=datetime.date.today)),
                ('notas', models.TextField(blank=True, null=True)),
            ],
        ),
    ]