from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import EventSerializer, UserSerializer
from .models import Event

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer