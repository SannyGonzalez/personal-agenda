# Generated by Django 4.2.1 on 2023-06-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='numero1',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='numero2',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='numero3',
            field=models.CharField(blank=True, null=True),
        ),
    ]
