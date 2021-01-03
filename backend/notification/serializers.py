from rest_framework import serializers

from spotify.models import Album
from youtube.models import Video
from spotify.serializers import AlbumSerializer
from youtube.serializers import VideoSerializer
from .models import Notification


class NotificationContentObjectSerializer(serializers.Field):

    def to_representation(self, value):
        if isinstance(value, Album):
            serializer = AlbumSerializer(value)
        elif isinstance(value, Video):
            serializer = VideoSerializer(value)
        else:
            raise Exception('Неподходящий тип content_object')

        return serializer.data


class NotificationSerializer(serializers.ModelSerializer):
    """
    Сериализует получение рекламы
    """
    content_type = serializers.SerializerMethodField('get_content_type_model')
    content_object = NotificationContentObjectSerializer()

    class Meta:
        model = Notification
        fields = '__all__'

    def get_content_type_model(self, obj):
        return obj.content_type.model
