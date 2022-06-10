# Generated by Django 2.2.24 on 2022-06-10 17:26

from django.db import migrations


def create_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            full_name=flat.owner_name,
            owners_phonenumber=flat.owner_pure_phone,
            owner_pure_phone=flat.owners_phonenumber,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220610_2318'),
    ]

    operations = [
        migrations.RunPython(create_owners,),
    ]
