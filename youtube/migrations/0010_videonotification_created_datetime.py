# Generated by Django 3.1.5 on 2021-05-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0009_remove_videonotification_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='videonotification',
            name='created_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
