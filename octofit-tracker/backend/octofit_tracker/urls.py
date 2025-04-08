from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, api_root

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),  # Add root endpoint
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
