# Generated by Django 3.1.4 on 2020-12-17 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0009_auto_20201215_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artist',
            new_name='author',
        ),
    ]
