# Generated by Django 3.1.4 on 2021-01-12 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0016_artistsubscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumnotification',
            options={'ordering': ['-creation_datetime']},
        ),
        migrations.RenameField(
            model_name='albumnotification',
            old_name='creation_time',
            new_name='creation_datetime',
        ),
    ]