from rest_framework import serializers

from .models import AlbumNotification, VideoNotification


class AlbumNotificationSerializer(serializers.ModelSerializer):
    """
    Сериализует оповещения об альбомах
    """

    class Meta:
        model = AlbumNotification
        fields = '__all__'


class VideoNotificationSerializer(serializers.ModelSerializer):
    """
    Сериализует оповещения о видео
    """

    class Meta:
        model = VideoNotification
        fields = '__all__'
