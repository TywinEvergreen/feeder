from rest_framework import serializers

from youtube.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    youtube_id = serializers.CharField()
    name = serializers.CharField(required=False)

    class Meta:
        model = Channel
        fields = "__all__"

    def create(self, validated_data) -> Channel:
        channel, _ = Channel.objects.get_or_create(
            youtube_id=validated_data.get("youtube_id"),
            defaults={"name": validated_data.get("name")},
        )
        return channel
