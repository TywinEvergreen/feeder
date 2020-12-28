# Generated by Django 3.1.4 on 2020-12-12 16:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0007_album_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, null=True, size=None),
        ),
    ]
