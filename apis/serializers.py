from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Event, UserProfile

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(use_url=True)
    class Meta:
        model = UserProfile
        fields = ('profile_photo',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    host = UserSerializer(many=False, read_only=True)
    time = serializers.DateTimeField()

    class Meta:
        model = Event
        fields = ('id', 'host', 'place_id', 'place_name', 'location', 'time')
        read_only_fields = ('id', 'place_name', 'location')

    def create(self, validated_data):
        return Event.objects.create_event(**validated_data)

