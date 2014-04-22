from main_app.models import Thing
from rest_framework import serializers

class ThingSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializing the Thing model for nice JSONiness
    """
    class Meta:
        model = Thing
        fields = ('created', 'title', 'body')