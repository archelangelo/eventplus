from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'host', 'place_id', 'location', 'time')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'events')