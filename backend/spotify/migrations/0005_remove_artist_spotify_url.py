# Generated by Django 3.1.4 on 2020-12-10 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0004_auto_20201209_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='spotify_url',
        ),
    ]
