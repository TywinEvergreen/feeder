# Generated by Django 3.1.4 on 2021-01-08 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0005_auto_20201222_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-release_datetime']},
        ),
        migrations.RenameField(
            model_name='video',
            old_name='release_date',
            new_name='release_datetime',
        ),
    ]