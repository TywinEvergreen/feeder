# Generated by Django 3.1.5 on 2021-05-09 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0006_auto_20210509_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videonotification',
            name='release_datetime',
        ),
    ]
