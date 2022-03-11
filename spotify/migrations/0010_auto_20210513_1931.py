# Generated by Django 3.1.5 on 2021-05-13 16:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("spotify", "0009_albumnotification_to"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="albumnotification",
            name="to",
        ),
        migrations.AddField(
            model_name="albumnotification",
            name="discarded_by",
            field=models.ManyToManyField(
                blank=True,
                related_name="discarded_album_notifications",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Отказавшиеся от уведомления",
            ),
        ),
        migrations.AddField(
            model_name="albumnotification",
            name="received_by",
            field=models.ManyToManyField(
                blank=True,
                related_name="received_album_notifications",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Получатели",
            ),
        ),
    ]
