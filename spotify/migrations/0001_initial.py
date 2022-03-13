# Generated by Django 4.0.3 on 2022-03-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('spotify_id', models.CharField(max_length=256, unique=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='album_covers')),
                ('type', models.CharField(choices=[('album', 'Альбом'), ('single', 'Сингл')], max_length=6)),
                ('release_datetime', models.DateTimeField()),
            ],
            options={
                'ordering': ['-release_datetime'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('spotify_id', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotify.album', verbose_name='Альбом')),
            ],
            options={
                'verbose_name_plural': 'Оповещения об альбомах',
                'ordering': ['-created_datetime'],
            },
        ),
    ]