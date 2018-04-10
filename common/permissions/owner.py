from rest_framework import permissions


class IsOwner(permissions.IsAuthenticated, permissions.BasePermission):
    """
    Allow access to the object only to it's owner.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.owner == user or user.is_staff
