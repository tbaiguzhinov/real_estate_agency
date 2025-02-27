# Generated by Django 2.2.24 on 2022-06-10 17:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220610_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner',
            new_name='owner_name',
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
