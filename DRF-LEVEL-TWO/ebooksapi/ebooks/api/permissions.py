from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view) # from the (IsAdminUser) - to check if the user is an admin or not
        return request.method in permissions.SAFE_METHODS or is_admin 
        # will return request.method that are not going to change the contents (if not an admin)


# to be able to edit the review made by the same user
class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.review_author == request.user
       