from rest_framework.permissions import (IsAuthenticated, BasePermission)


class IsAuthenticatedAndActive(IsAuthenticated):
    def has_permission(self, request, view):
        if super():
            return bool(request.user.is_active)
        return False


class PostOnlyUnAuth(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'


class GetOnlyUnAuth(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'
