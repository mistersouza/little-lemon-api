from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MenuItemViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'menu-items', MenuItemViewSet, basename='menuitems')

urlpatterns = [
    path('', include(router.urls)),
]