from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperuserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsOwnerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.customer.user


class CustomIsAuthenticatedOrReadOnly(BasePermission):

    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')

    def has_permission(self, request, view):
        return bool(
            request.method in self.SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )