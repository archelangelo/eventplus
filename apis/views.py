from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserEvent(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        pass