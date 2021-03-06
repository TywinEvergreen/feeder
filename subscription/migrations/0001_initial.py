# Generated by Django 3.1.4 on 2021-01-21 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_committed', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-datetime_committed'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChannelSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_committed', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.channel')),
            ],
            options={
                'ordering': ['-datetime_committed'],
                'abstract': False,
            },
        ),
    ]
