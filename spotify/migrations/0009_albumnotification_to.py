# Generated by Django 3.1.5 on 2021-05-12 17:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spotify', '0008_albumnotification_created_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumnotification',
            name='to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Получатели'),
        ),
    ]
