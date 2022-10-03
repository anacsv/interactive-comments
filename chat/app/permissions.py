from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = view.request.user

        if user.is_superuser:
            return True
        else:
            return request.method not in ('DELETE',)

class IsSameUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = view.request.user
        model_user = obj.username

        if request.method in ('PUT', 'DELETE',) and (user.is_superuser or user.id == model_user.id):
            return super().has_object_permission(request, view, obj)
        else:
            return False
