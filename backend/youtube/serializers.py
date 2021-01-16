from rest_framework import serializers

from user.models import User
from .models import Channel, Video, ChannelSubscription, \
    VideoNotification


class ChannelSerializer(serializers.ModelSerializer):
    """
    Сериализует каналы
    """
    youtube_id = serializers.CharField()
    name = serializers.CharField(required=False)

    class Meta:
        model = Channel
        fields = '__all__'


    def create(self, validated_data):
        channel, _ = Channel.objects.get_or_create(
            youtube_id=validated_data.get('youtube_id'),
            defaults={
                'name': validated_data.get('name')
            }
        )
        return channel


class ChannelSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализует подписки на каналы
    """
    subscriber = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = ChannelSubscription
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        subscription = ChannelSubscription.objects.create(**validated_data, subscriber=user)
        return subscription


class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()

    class Meta:
        model = Video
        fields = '__all__'


class VideoNotificationSerializer(serializers.ModelSerializer):
    """
    Сериализует оповещения о видео
    """

    class Meta:
        model = VideoNotification
        fields = '__all__'