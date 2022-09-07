# Generated by Django 4.1 on 2022-09-06 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_rename_image_country_country_image'),
        ('places', '0002_places_image_alter_placeimage_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_from_country', to='countries.country'),
        ),
    ]