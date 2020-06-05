from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer, ActivityPeriodSerializer

from . import views
from .models import User

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'activities', views.ActivityPeriodViewSet)
router.register(r'all', views.TimelineViewSet, basename='MyModel')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]