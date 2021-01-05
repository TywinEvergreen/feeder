from rest_framework import serializers

from youtube.models import Channel, Video


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
            youtube_id=validated_data['youtube_id'],
            defaults={
                'name': validated_data.get('name')
            }
        )
        return channel


class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()

    class Meta:
        model = Video
        fields = '__all__'

