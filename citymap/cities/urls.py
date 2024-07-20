from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CityViewSet, StreetViewSet, ShopViewSet


router = SimpleRouter()

router.register(r'city', CityViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('city/<int:city_id>/street/', StreetViewSet.as_view({'get': 'list'})),
]