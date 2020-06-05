 #serializers.py
from rest_framework import serializers

from .models import User, ActivityPeriod

class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
	start_time = serializers.DateTimeField()
	end_time = serializers.DateTimeField()
	class Meta:
		model = ActivityPeriod
		fields = ('start_time', 'end_time')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	activityperiods = ActivityPeriodSerializer(many=True, read_only=True)
	# id = serializers.CharField(source='uid')

	class Meta:
		model = User
		fields = ['id', 'real_name', 'tz', 'activityperiods', ]

class TimelineSerializer(serializers.Serializer):
    members = UserSerializer(many=True)
    ok = serializers.BooleanField(initial=True)
