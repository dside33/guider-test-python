from rest_framework.serializers import ModelSerializer, CharField

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
    city = CharField(source='city.name', read_only=True)
    street = CharField(source='street.name', read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'house_number', 'name', 'open_time', 'close_time', 'city', 'street']