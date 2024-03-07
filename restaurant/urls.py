from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, TableViewSet

router = DefaultRouter()
router.register(r'menus', MenuViewSet)
router.register(r'tables', TableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
