from rest_framework import routers, serializers, viewsets
from app.models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class Nearest(serializers.Serializer):
    id = serializers.IntegerField()
    formatted_address = serializers.CharField()
    city = serializers.CharField()
    info = serializers.CharField()
    distance_km = serializers.CharField()

