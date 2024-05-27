

from rest_framework import routers
from app.rest.viewsets import AddressViewset
router = routers.DefaultRouter()
router.register(r'address_book', AddressViewset, basename= 'user')
