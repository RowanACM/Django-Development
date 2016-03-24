from __future__ import unicode_literals

from django.db import models

# Create Your Models Here

class Member(models.Model):
    serial = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    meetings_attend = models.IntegerField(default=0)

