from django.contrib import admin

from django.contrib import admin
from .models import Role, Permission, Module, RolePermission, UserRole, UserPermission

admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Module)
admin.site.register(RolePermission)
admin.site.register(UserRole)
admin.site.register(UserPermission)
