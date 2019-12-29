from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    host = UserSerializer(many=False, read_only=True)
    time = serializers.DateTimeField()

    class Meta:
        model = Event
        fields = ('id', 'host', 'place_id', 'place_name', 'location', 'time')
        read_only_fields = ('id', 'place_name', 'location')

    def create(self, validated_data):
        return Event.objects.create_event(**validated_data)

