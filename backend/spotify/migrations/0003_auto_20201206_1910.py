# Generated by Django 3.1.4 on 2020-12-06 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_auto_20201206_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='last_album',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='spotify.artist'),
            preserve_default=False,
        ),
    ]
