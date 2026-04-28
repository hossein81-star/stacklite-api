
from rest_framework.permissions import BasePermission


class IsActivatedUser(BasePermission):
    def has_permission(self, request, view):
        message='your email is not verified'
        return bool(request.user and request.user.is_authenticated and request.user.is_verified)