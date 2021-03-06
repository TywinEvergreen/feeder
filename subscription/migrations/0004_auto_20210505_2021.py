# Generated by Django 3.1.5 on 2021-05-05 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_videonotification'),
        ('subscription', '0003_auto_20210122_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelsubscription',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='youtube.channel'),
        ),
    ]
