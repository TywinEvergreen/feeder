from rest_framework import permissions


class IsCurrentUserOrReadOnly(permissions.BasePermission):
    """
    Пропускает только этого пользователя ( request.user )
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS or
                obj.id is request.user.id)
