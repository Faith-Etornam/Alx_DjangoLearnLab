from rest_framework.permissions import BasePermission

class IsOwnwerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS for everyone
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Write permissions for only the owner
        return obj.owner == request.user