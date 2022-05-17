# Generated by Django 2.2.24 on 2022-05-16 18:44

from django.db import migrations


class Migration(migrations.Migration):
    def create_owners(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        Owner = apps.get_model('property', 'Owner')
        for flat in Flat.objects.all():
            Owner.objects.get_or_create(
                name = flat.owner_name,
                phonenumber = flat.owners_phonenumber,
                pure_phonenumber = flat.owner_pure_phone
            )

    dependencies = [
        ('property', '0012_auto_20220516_2133'),
    ]

    operations = [
        migrations.RunPython(create_owners)
    ]
