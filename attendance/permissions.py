from rest_framework import permissions, request


# class IsLecturer(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.Student == request.user

class IsLecturer(permissions.BasePermission):
    message = "You are not a Lecturer"

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list("name", flat=True)
        if "Lecturer" in user_groups:
            return True
        return False
