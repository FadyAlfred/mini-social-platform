from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to authenticate the owner of an object
    """
    def has_permission(self, request, view):
        return request.user

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user