from rest_framework.permissions import BasePermission, SAFE_METHODS, DjangoModelPermissions

class IsAdminOrUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True 
        return request.user and request.user.is_staff

class FullDjangoModelPermission(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


class IsAuthorOrReadonly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated # normal user
    
    def has_object_permission(self, request, view, obj): # admin user
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        
        return obj.user == request.user
