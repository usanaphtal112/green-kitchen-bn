from rest_framework.permissions import BasePermission


class IsUnauthenticated(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class AdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the "admin" role
        return request.user.role == "admin"
