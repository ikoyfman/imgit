from rest_framework import permissions


class is_author_or_admin(permissions.BasePermission):

    # Check if token passed is equal author id or is admin user
    def has_object_permission(self, request, view, obj):

        # check if author id is equal
        if request.user == obj.author:
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False
