from django.db import models

# Create your models here.
# models.py
from django.db import models
# from django.utils.crypto import get_random_string
  

class User(models.Model):
	id = models.AutoField(primary_key=True)
	real_name = models.CharField(max_length=60)
	tz = models.CharField(max_length=60)


	# def save(self, *args, **kwargs):
	# 	id = self.id
	# 	if not id:
	# 		id = get_random_string(length=9)
	# 	while User.objects.filter(id=id).exclude(pk=self.pk).exists():
	# 		id = get_random_string(length=9)
	# 		self.id = id
	# 	super(User, self).save(*args, **kwargs)

class ActivityPeriod(models.Model):
	id = models.AutoField(primary_key=True)
	start_time = models.TimeField()
	end_time = models.TimeField()
	user = models.ForeignKey(User, related_name='activityperiods', on_delete=models.CASCADE)

	class Meta:
		unique_together = ['user', 'id']
		ordering = ['id']

	def __str__(self):
		return '%s: %s' % (self.start_time, self.end_time)