# Generated by Django 2.2.24 on 2022-06-10 18:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20220610_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]
