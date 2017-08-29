from django.db import models
from django.core.urlresolvers import reverse

class Info(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=225)
	email = models.CharField(max_length=50)

	def get_absolute_url(self):
   	    return reverse('create')