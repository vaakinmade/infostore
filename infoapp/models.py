"""
This project uses django 1.11 and therefore leverages the capabilities provided by the same.

1. Older versions of django would have required importing the validate_email component to
explicitly apply email validation to the email field. However v1.11 implements validation
on the email once the EmailField is used. 

2. get_absolute_url is used as opposed to setting a success_url on the CreateView. Either
approach would have sufficed. 
"""

from django.db import models
from django.core.urlresolvers import reverse


class Info(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=225)
	email = models.EmailField(max_length=50)

	def get_absolute_url(self):
   	    return reverse('create')