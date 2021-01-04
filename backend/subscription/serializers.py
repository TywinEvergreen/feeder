from rest_framework import serializers

from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализует подписки
    """

    class Meta:
        model = Subscription
        fields = '__all__'

    # def get_content_type_model(self, obj):
    #     return obj.content_type.model
