# Generated by Django 4.2.1 on 2023-06-29 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_eventos_contacto_rel'),
        ('contactos', '0005_contacto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contactos',
        ),
    ]
