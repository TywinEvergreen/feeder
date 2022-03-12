from rest_framework import serializers

from youtube.models import Video, VideoNotification
from youtube.serializers.channel import ChannelSerializer


class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()

    class Meta:
        model = Video
        fields = "__all__"


class VideoNotificationSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = VideoNotification
        fields = "__all__"
