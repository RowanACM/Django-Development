from __future__ import unicode_literals

from django.db import models

<<<<<<< HEAD
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    meetings_attend = models.IntegerField(0)
=======

class Member(models.Model):
    	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	meeting_attend = 0
>>>>>>> f986dd158f6425084296b38923cdb173b25f7e64
