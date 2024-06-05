from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    def has_permission(self, request, view):
        # Allow if the user is authenticated and has a 14-digit username
        return request.user.is_authenticated and len(request.user.username) == 14
