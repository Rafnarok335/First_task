# Generated by Django 4.1.3 on 2022-11-28 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]
