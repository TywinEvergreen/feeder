from rest_framework import permissions


class OnlyCurrentUserSubscriptions(permissions.BasePermission):
    """
    Пропускает подписки данного пользователя
    """

    def has_object_permission(self, request, view, obj):
        return obj.subscriber.pk is request.user.pk