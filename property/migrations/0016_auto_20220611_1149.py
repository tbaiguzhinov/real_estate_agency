# Generated by Django 2.2.24 on 2022-06-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220611_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_name',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(
                blank=True,
                to='property.Flat',
                verbose_name='Квартиры в собственности'
            ),
        ),
    ]
