# Generated by Django 4.1 on 2022-09-09 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_places_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='hotel',
        ),
    ]
