from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create Your Models Here

class Member(models.Model):
    serial = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    meetings_attend = models.IntegerField(default=0)

class Meetings(models.Model):
    serial_ID = models.CharField(max_length=20)
    meeting_Date = models.DateTimeField(default=datetime.now())


