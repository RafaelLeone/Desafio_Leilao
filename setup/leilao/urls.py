from django.urls import include, path
from rest_framework import status
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .views import ItemViewSet, RealEstateDetailView, RealEstateEditView, RegisterView, LoginView, LogoutView, ItemDetailView, ItemEditView, RealEstateViewSet, VehicleDetailView, VehicleEditView, VehicleViewSet, UserViewSet, UserDetailView
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import RealEstate


router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'realestates', RealEstateViewSet)
router.register(r'vehicles', VehicleViewSet)
# router.register(r'users', UserViewSet)

def pega_usuario(request, username):
    return JsonResponse(dict(user_id=User.objects.get(username=username).id))

@api_view(['POST'])
def add_bid(request, realestate_id):
    try:
        real_estate = RealEstate.objects.get(id=realestate_id)
        print(f'history {RealEstate.objects.get(id=realestate_id).bid_history}')
        bid_data = request.data
        user = request.user.username
        bid = {
            "user": user,
            "bid": bid_data['bid']
        }
        print(f'history {real_estate.bid_history}')
        if not real_estate.bid_history:
            print('entra aqii')
            real_estate.bid_history = []
        real_estate.bid_history.append(bid)
        print(f'history {real_estate.bid_history}')
        print(f'bid {bid}')
        real_estate.save()
        print(f'updated history {RealEstate.objects.get(id=realestate_id).bid_history}')
        return Response({"message": "Bid added"}, status=status.HTTP_200_OK)
    except RealEstate.DoesNotExist:
        return Response({"error": "Real estate not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/items/<int:item_id>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/edit/<int:item_id>/', ItemEditView.as_view(), name='item-edit'),
    path('users/<str:username>/', pega_usuario, name='user-detail'),
    path('realestates/<int:realestate_id>/', RealEstateDetailView.as_view(), name='real-estate-detail'),
    path('realestates/<int:realestate_id>/edit/', RealEstateEditView.as_view(), name='real-estate-edit'),
    path('vehicles/<int:vehicle_id>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicles/<int:vehicle_id>/edit/', VehicleEditView.as_view(), name='vehicle-edit'),
    path('realestates/<int:realestate_id>/add_bid/', add_bid, name='add-bid')
]
