# Generated by Django 3.2.11 on 2022-01-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hks', '0002_profile_details_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user1',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='user1',
            name='is_Dcotor',
            field=models.BooleanField(default=False, verbose_name='Docotr status'),
        ),
        migrations.AddField(
            model_name='user1',
            name='is_Patient',
            field=models.BooleanField(default=False, verbose_name='Patient status'),
        ),
    ]
