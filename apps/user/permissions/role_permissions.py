from rest_framework.permissions import BasePermission

from apps.user.models import UserRole


class IsAdmin(BasePermission):

    message = "Only administrators can perform this action."

    def has_permission(self, request, view):
        
        return (
            request.user.is_authenticated
            and request.user.role == UserRole.ADMIN
        )