"""redzitta URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Router
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('events/nearby/', views.NearbyEvents.as_view(), name='event-nearby'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('places/nearby/', views.GoogleAPINearbyView.as_view(), name='place-nearby'),
    path('places/textsearch/', views.GoogleAPITextsearchView.as_view(), name='place-textsearch'),
]

handler400 = 'rest_framework.exceptions.bad_request'