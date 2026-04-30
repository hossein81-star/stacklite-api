
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorUser(BasePermission):
    message = "just Author can view this page"

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS and request.method == 'POST':
            return True


        if not request.user or not request.user.is_authenticated:
            return False


        else:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user



class IsActivatedUser(BasePermission):
    def has_permission(self, request, view):
        message='your email is not verified'
        return bool(request.user and request.user.is_authenticated and request.user.is_verified)