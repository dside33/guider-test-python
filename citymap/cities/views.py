from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .filters import ShopFilter
from .models import City, Street, Shop
from .serializers import (
                        CitySerializer, 
                        StreetSerializer, 
                        ShopSerializer
                        )


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class StreetViewSet(ModelViewSet):
    queryset = Street.objects.all()

    def list(self, request, *args, **kwargs):
        city_id = self.kwargs.get('city_id')
        if city_id:
            streets = Street.objects.filter(city_id=city_id)
        else:
            streets = Street.objects.all()
        
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def list(self, request):
        filtered_queryset = ShopFilter(request.GET, queryset=self.get_queryset()).qs
        
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            shop = serializer.save() 
            return Response({'id': shop.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        