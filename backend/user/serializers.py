from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализует пользователей
    """

    class Meta:
        model = User
        fields = '__all__'