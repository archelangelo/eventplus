from django.contrib.auth.models import User
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from django.http.response import HttpResponseNotAllowed, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from .serializers import EventSerializer, UserSerializer
from .models import Event
from .google_apis import Client

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=False, methods=['get'])
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

    def create(self, request):
        return Response({'status': 'in progress'})

class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get', 'post'])
    def events(self, request, pk=None):
        if request.method == 'POST':
            return self.create_event(request, pk)
        if request.method == 'GET':
            return self.get_events(request, pk)
        return Response({'status': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create_event(self, request, pk):
        user = self.get_object()
        place_id = request.data.get('place_id', None)
        if place_id == None:
            return Response({'status': 'bad place id'}, status=status.HTTP_400_BAD_REQUEST)
        event = Event.objects.create_event(host=user, place_id=place_id)
        event.save()
        return Response(data={'status': 'created'})

    def get_events(self, request, pk):
        return Response({'status', 'in progress'})

class GoogleAPINearbyView(APIView):
    
    def get(self, request):
        params = request.query_params
        try:
            location = params['location']
        except KeyError:
            raise ValidationError(detail='Bad location parameter.')
        radius = params.get('radius', 1500)
        response_body = Client.nearby_request(location=location, radius=radius)
        return Response(data=response_body)

class GoogleAPITextsearchView(APIView):
    
    def get(self, request):
        params = request.query_params
        try:
            query = params['query']
        except KeyError:
            raise ValidationError(detail='Bad query parameter.')
        location = params.get('location', None)
        radius = params.get('radius', None)
        response_body = Client.textsearch_request(query, location, radius)
        return Response(data=response_body)
