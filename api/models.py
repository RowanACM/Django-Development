from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create Your Models Here

class Member(models.Model):
    """
    Model for Members of our club
    serial is unique from Rowan ID Card
    first_name and last_name are given by new memeber
    meettings_attended is a number defaulting to 0 when they initially sign up
    """
    serial = models.CharField(max_length=20)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    meetingsAttended = models.IntegerField(default=0)

class Meetings(models.Model):
    """
    Model for club meetings attended
    serial is from Rowan ID Card
    meetingDate is date and time of meeting attended
    """
    serial = models.CharField(max_length=20)
    meetingDate = models.DateTimeField(default=datetime.now())


