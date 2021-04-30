# Generated by Django 3.1.4 on 2021-01-21 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('youtube_id', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('youtube_id', models.CharField(max_length=256, unique=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='video_covers')),
                ('release_datetime', models.DateTimeField()),
                ('channel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='youtube.channel')),
            ],
            options={
                'ordering': ['-release_datetime'],
            },
        ),
    ]