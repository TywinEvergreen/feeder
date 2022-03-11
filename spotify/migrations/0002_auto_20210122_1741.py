# Generated by Django 3.1.4 on 2021-01-22 14:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("spotify", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="album",
            options={"ordering": ["-release_datetime"]},
        ),
        migrations.RemoveField(
            model_name="album",
            name="release_date",
        ),
        migrations.AddField(
            model_name="album",
            name="release_datetime",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 1, 22, 14, 41, 16, 170534, tzinfo=utc)
            ),
            preserve_default=False,
        ),
    ]
