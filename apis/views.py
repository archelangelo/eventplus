from django.contrib.auth.models import User
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import EventSerializer, UserSerializer
from .models import Event

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @action(detail=False)
    def nearby(self, request):
        params = request.query_params
        try:
            lng = float(params['lng'])
            lat = float(params['lat'])
            distance = float(params['dist'])
        except KeyError:
            raise ValidationError(detail='Bad query parameters.')

        location = GEOSGeometry('POINT({} {})'.format(lng, lat), srid=4326)
        queryset = Event.objects.filter(location__distance_lte=(location, D(km=distance)))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer