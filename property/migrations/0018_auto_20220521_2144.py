# Generated by Django 2.2.24 on 2022-05-21 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20220521_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_flats',
            new_name='flats',
        ),
    ]