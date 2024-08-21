from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter(trailing_slash=False)
router.register(r'menu-items', MenuItemViewSet, basename='menuitems')
router.register(r'cart', CartViewSet, basename='carts')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'users', UserViewSet, basename='users')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('', include(router.urls)),
]