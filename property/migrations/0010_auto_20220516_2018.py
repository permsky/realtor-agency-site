# Generated by Django 2.2.24 on 2022-05-16 17:18

import phonenumbers
from django.db import migrations


class Migration(migrations.Migration):
    def normalize_phonenumbers(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        flats = Flat.objects.all()
        if flats.exists():
            for flat in flats.iterator():
                parsed_phonenumber = phonenumbers.parse(
                    flat.owners_phonenumber,
                    region='RU'
                )
                if phonenumbers.is_valid_number(parsed_phonenumber):
                    flat.owner_pure_phone = parsed_phonenumber
                else:
                    flat.owner_pure_phone = None
                flat.save()

    dependencies = [
        ('property', '0009_auto_20220516_2004'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumbers)
    ]
