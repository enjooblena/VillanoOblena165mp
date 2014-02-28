from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class newPerson(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	age = models.IntegerField()
	address = models.CharField(max_length=120, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode(self):
		return self.first_name