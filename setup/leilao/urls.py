from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, RegisterView, LoginView, LogoutView, ItemDetailView, ItemEditView, RealEstateViewSet, VehicleViewSet, UserViewSet, UserDetailView
from django.contrib.auth.models import User
from django.http import JsonResponse


router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'realestates', RealEstateViewSet)
router.register(r'vehicles', VehicleViewSet)
# router.register(r'users', UserViewSet)

def pega_usuario(request, username):
    return JsonResponse(dict(user_id=User.objects.get(username=username).id))

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/items/<int:item_id>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/edit/<int:item_id>/', ItemEditView.as_view(), name='item-edit'),
    path('users/<str:username>/', pega_usuario, name='user-detail'),
]
