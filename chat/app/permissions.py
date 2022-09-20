from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = view.request.user

        if user.is_superuser:
            return True
        else:
            return request.method not in ('DELETE',)
