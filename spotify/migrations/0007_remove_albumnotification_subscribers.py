# Generated by Django 3.1.5 on 2021-05-11 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("spotify", "0006_remove_albumnotification_release_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="albumnotification",
            name="subscribers",
        ),
    ]
