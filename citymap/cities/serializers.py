from rest_framework.serializers import ModelSerializer

from .models import City, Street, Shop


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class StreetSerializer(ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'