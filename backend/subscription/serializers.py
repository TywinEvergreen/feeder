from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from spotify.serializers import ArtistSerializer
from youtube.serializers import ChannelSerializer
from user.serializers import UserSerializer
from spotify.models import Artist
from youtube.models import Channel
from .models import Subscription


class SubscriptionAuthorObjectSerializer(serializers.Field):

    def to_representation(self, value):
        if isinstance(value, Artist):
            serializer = ArtistSerializer(value)
        elif isinstance(value, Channel):
            serializer = ChannelSerializer(value)
        else:
            raise Exception('Неподходящий тип auhtor_object')

        return serializer.data


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализует подписки
    """
    author_type_str = serializers.CharField(required=False)

    # author_type = serializers.CharField(source='content_type.model', required=False)
    author_type = serializers.SerializerMethodField('get_author_type_model')
    author_object = SubscriptionAuthorObjectSerializer(required=False)
    subscriber = UserSerializer(required=False)

    class Meta:
        model = Subscription
        fields = '__all__'

    def get_author_type_model(self, obj):
        return obj.author_type.model

    def create(self, validated_data):
        subscription, _ = Subscription.objects.get_or_create(
            author_type=ContentType.objects.get(
                model=validated_data['author_type_str']
            ),
            author_id=validated_data['author_id'],
            subscriber=self.context.get('request').user
        )
        return subscription
