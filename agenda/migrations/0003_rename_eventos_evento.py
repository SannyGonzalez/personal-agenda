# Generated by Django 4.2.1 on 2023-06-29 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0006_delete_contactos'),
        ('agenda', '0002_alter_eventos_contacto_rel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eventos',
            new_name='Evento',
        ),
    ]
