# Generated by Django 3.2.11 on 2022-01-30 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hks', '0004_remove_profile_details_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user1',
            old_name='is_Dcotor',
            new_name='is_Doctor',
        ),
    ]
