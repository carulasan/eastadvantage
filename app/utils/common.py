from django.conf import settings
from rest_framework.permissions import IsAuthenticated
# viewset permission
permission = [] if settings.ENV == 'local' else [IsAuthenticated]
