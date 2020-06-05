from django.db import models

from django.db import IntegrityError
import string 
import random 
  

class User(models.Model):
	id = models.AutoField(primary_key=True)
	real_name = models.CharField(max_length=60)
	tz = models.CharField(max_length=60)

class ActivityPeriod(models.Model):
	id = models.AutoField(primary_key=True)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	user = models.ForeignKey(User, related_name='activityperiods', on_delete=models.CASCADE)

	class Meta:
		unique_together = ['user', 'id']
		ordering = ['id']

	def __str__(self):
		return '%s: %s' % (self.start_time, self.end_time)