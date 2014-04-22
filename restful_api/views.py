from rest_framework import viewsets
from main_app.models import Thing
from restful_api.serializers import ThingSerializer

class ThingViewSet(viewsets.ModelViewSet):
    """
    an API endpoint for the Thing model
    """
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
