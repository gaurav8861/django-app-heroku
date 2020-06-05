from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.core import serializers


from .serializers import UserSerializer, ActivityPeriodSerializer, TimelineSerializer
from .models import User, ActivityPeriod
from django.http import JsonResponse
from django.views.generic import ListView

from django.shortcuts import render
from django.core import serializers
from rest_framework.response import Response
from django.http import HttpResponse
from .models import User
import json
from rest_framework.decorators import api_view

from rest_framework.views import APIView

from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from collections import namedtuple

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer

class TimelineViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing the Tweets and Articles in your Timeline.
    """
    def list(self, request):
        Timeline = namedtuple('Timeline', ('ok', 'members'))
        timeline = Timeline(
            ok=True,
            members=User.objects.all(),
        )
        serializer = TimelineSerializer(timeline, context={'request': request})
        return Response(serializer.data)

# class AllViewSet(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

    # # serializer_context = {'request': Request(request._request)}

    # def list(self, request, *args, **kwargs):
    #     # User_list = User.objects.all()
    #     # # serializer_class = UserSerializer
    #     # # for user in User_list:
    #     # #     userInfo = User.objects.filter(id=user.pk)
    #     # #     user_serializer = UserSerializer(userInfo, many=True)
    #     # #     activity_list = ActivityPeriod.objects.filter(user=user.pk)

    #     # # user_dic = {
    #     # #     	'ok':True,
    #     # #         'members': User_list
    #     # # }
    #     # # data_a = json.dumps(User_list)
    #     # data = serializers.serialize('json', self.get_queryset())
    #     # # data = serializers.serialize('json', self.get_queryset())

    #     # # prices = Price.objects.filter(product=product).values_list('price','valid_from')


    #     # content = JSONRenderer().render(data)

    #     # # data = json.dumps(User_list)
    #     # return JsonResponse(content, safe=False)
    #     # queryset = User.objects.all()
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     # return Response(serializer.data)

    #     data = {
    #         'ok':True,
    #         'members': serializer.data
    #     }
    #     return JsonResponse(data)