from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from app.utils.location import distanceKm


from app.models import Address
from app.rest.serializers import AddressSerializer, Nearest
from rest_framework.decorators import action
from rest_framework.response import Response

#Decimal
from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().prec = 6
decimal_places = Decimal('0.001')  # This corresponds to 2 decimal places

class AddressViewset(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = None
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['formatted_address',]  
    filterset_fields = ['city']
    ordering_fields = ['date_updated']

    @action(detail=False, methods=['get'])
    def nearest(self, request, pk=None):
        distance = float(request.query_params.get('distance'))
        long = float(request.query_params.get('long'))
        lat = float(request.query_params.get('lat'))
        addresses = []
        start = {
            'long' : long,
            'lat' : lat
        }
        for instance in Address.objects.all():
            end = {
                'long' : instance.long,
                'lat' : instance.lat
            }
            d_km = distanceKm(start,end)
            if(float(d_km) <= distance):
                number = Decimal(d_km)
                nearest = {
                    'id' : instance.id,
                    'formatted_address': instance.formatted_address,
                    'city' : instance.city,
                    'info' : f"Near of the location in total of {number.quantize(decimal_places, rounding=ROUND_HALF_UP)} Kilometer/s",
                    'distance_km' : d_km
                }
                addresses.append(nearest)
        nearest_sort = sorted(addresses, key=lambda x: x['distance_km'], reverse=False)           
        serialize = Nearest(data=nearest_sort , many=True)
        if serialize.is_valid():
            return Response(serialize.data)
        else:
            return Response(serialize.error_messages)

