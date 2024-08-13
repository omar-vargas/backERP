
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, PermissionViewSet, ModuleViewSet, RolePermissionViewSet, UserRoleViewSet, UserPermissionViewSet

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'rolepermissions', RolePermissionViewSet)
router.register(r'userroles', UserRoleViewSet)
router.register(r'userpermissions', UserPermissionViewSet)

urlpatterns = router.urls

