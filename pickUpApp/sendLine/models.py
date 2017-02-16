from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PickUpLine(models.Model):
	line = models.TextField()

	def __unicode__(self):
		return self.line