from __future__ import unicode_literals

from django.db import models

# Create Your Models Here

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    meetings_attend = models.IntegerField(0)

