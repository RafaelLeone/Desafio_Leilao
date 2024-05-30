from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, RegisterView, LoginView, LogoutView, ItemDetailView


router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/items/<int:item_id>/', ItemDetailView.as_view(), name='item-detail'),
]
