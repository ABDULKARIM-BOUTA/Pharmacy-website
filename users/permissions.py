from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow admin to do anything
        if request.user and request.user.is_staff:
            return True
        # Allow user to access their own orders
        return obj.user == request.user