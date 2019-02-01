from rest_framework import serializers
from .models import *


class HeadsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = heads
        fields = ('name',)

class SubHeadSerializer(serializers.ModelSerializer):

    class Meta:
        model=subheads
        fields=('head','name',)