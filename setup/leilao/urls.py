from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet


router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]
