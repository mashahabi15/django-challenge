from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    """
    A custom permission for checking whether the user is superuser or not
    """

    def has_permission(self, request, view):
        return request.user.is_superuser
