from rest_framework import serializers

from subscription.serializers import SubscriptionSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализует пользователей
    """
    subscriptions = SubscriptionSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     allowed_arguements = ['artist', 'channel']
    #
    #     for item in validated_data.items():
    #         if item[0] in allowed_arguements:
    #             if item[0] == 'artist':
    #                 artist = Artist.objects.get(spotify_id=item[1])
    #                 if instance.followed_artists.filter(pk=artist.pk):
    #                     instance.followed_artists.remove(artist)
    #                 else:
    #                     instance.followed_artists.add(artist)
    #             elif item[0] == 'channel':
    #                 channel = Channel.objects.get(youtube_id=item[1])
    #                 if instance.followed_channels.filter(pk=channel.pk):
    #                     instance.followed_channels.remove(channel)
    #                 else:
    #                     instance.followed_channels.add(channel)
    #             else:
    #                 setattr(instance, item[0], item[1])
    #
    #     instance.save()
    #     return instance
