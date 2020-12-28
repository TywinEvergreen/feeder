from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Сериализует получение рекламы
    """

    class Meta:
        model = Notification
        fields = '__all__'
