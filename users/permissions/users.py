"""User permissions."""

#Django REST Framework
from rest_framework.permissions import BasePermission

class IsAccountOwner(BasePermission):
    """Allow acccess only to objects owned by the requiring user."""

    def has_object_permission(self, request, view, obj):
        """Check user and object are the same"""
        return request.user == obj
