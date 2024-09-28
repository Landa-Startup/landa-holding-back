from rest_framework import permissions

class CanViewVacation(permissions.BasePermission):
    edit_methods = ['GET']
    def has_permission(self, request, view):
        return request.user.has_perm('panel.can_view_vacation')

class CanCreateVacation(permissions.BasePermission):
    edit_methods = ['POST']
    def has_permission(self, request, view):
        return request.user.has_perm('panel.can_create_vacation')

class CanEditVacation(permissions.BasePermission):
    edit_methods = ['PUT']
    def has_permission(self, request, view):
        return request.user.has_perm('panel.can_edit_vacation')
    
class CanDeleteVacation(permissions.BasePermission):
    edit_methods = ['DELETE']
    def has_permission(self, request, view):
        return request.user.has_perm('panel.can_delete_vacation')

class CanGetAllVacation(permissions.BasePermission):
    edit_methods = ['GET']
    def has_permission(self, request, view):
        return request.user.has_perm('panel.can_get_all_vacation')
