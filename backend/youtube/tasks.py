from __future__ import absolute_import, unicode_literals
from django.core.files.base import ContentFile
from django.contrib.contenttypes.models import ContentType
from urllib.parse import urlparse
import requests
import datetime

from dateutil.parser import parse

from feeder.settings import YOUTUBE
from feeder.celery import app
from feeder.utils import delete_related_files
from notification.models import Notification
from .models import Channel, Video


@app.task
def get_new_videos():
    """
    Обновляет youtube видео в базе данных на полученные из Youtube API
    """
    for channel in Channel.objects.all():
        newest = YOUTUBE.search().list(
            channelId=channel.youtube_id, maxResults=1,
            part='snippet', order='date'
        ).execute()['items'][0]['snippet']

        if not hasattr(channel, 'video') or \
           channel.video.release_datetime < parse(newest['publishedAt']):

            if hasattr(channel, 'video'):
                delete_related_files(channel.video)
                channel.video.delete()

            new_video = Video.objects.create(
                name=newest['title'],
                youtube_id=newest['channelId'],
                channel=channel,
                release_datetime=parse(newest['publishedAt'])
            )

            cover_url = newest['thumbnails']['high']['url']
            cover_file = ContentFile(requests.get(cover_url).content)
            new_video.cover.save(f'{newest["publishedAt"]}_{new_video.name}_cover.jpg', cover_file)

            Notification.objects.create(
                content_type=ContentType.objects.get_for_model(new_video),
                object_id=new_video.pk
            )
