# Generated by Django 3.1.5 on 2021-05-11 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0008_auto_20210511_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videonotification',
            name='subscribers',
        ),
    ]
