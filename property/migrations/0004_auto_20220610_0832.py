# Generated by Django 2.2.24 on 2022-06-10 02:32

from django.db import migrations


def identify_new_buildings(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    all_flats = Flat.objects.all()
    for flat in all_flats.iterator():
        flat.new_building = (flat.construction_year >= 2015)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(identify_new_buildings,),
    ]
