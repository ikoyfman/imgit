from rest_framework import permissions
import pdb; 

class is_author(permissions.BasePermission):

    # Check if token passed is equal author id or is admin user
    def authenticate(self, request, view, obj):
        # check if author id is equal
        token = request.META
        pdb.set_trace()
        return True
