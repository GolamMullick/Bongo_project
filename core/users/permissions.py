  
from rest_framework import permissions
from .models import User
from rest_framework.permissions import IsAuthenticated



class IsAdmin(permissions.BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return User.USER_TYPES_MAP['admin'] == request.user.user_type

class IsRestaurant(permissions.BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return User.USER_TYPES_MAP['restaurant'] == request.user.user_type

class IsEmployee(permissions.BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return User.USER_TYPES_MAP['employee'] == request.user.user_type


