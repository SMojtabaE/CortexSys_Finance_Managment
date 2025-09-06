from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):

        # Write and read is only allowed to the owner of the budgets.
        return obj.user == request.user