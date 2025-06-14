from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    """
    Allow access only to users with role as  seller
    """
    def has_permission(self, request, view):
        user = request.user
        is_authenticated = user.is_authenticated
        if hasattr(user, 'role'):
            is_seller = user.role=='seller'
        else:
            is_seller = False
        return is_authenticated and is_seller