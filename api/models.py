from __future__ import unicode_literals

from django.db import models


class Member(models.Model):
    	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	meeting_attend = 0
