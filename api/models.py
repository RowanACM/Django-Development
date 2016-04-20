from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create Your Models Here

class Member(models.Model):
    """
    Model for Members of our club
    serial is unique from Rowan ID Card
    first_name and last_name are given by new member
    meetings_attended is a number defaulting to 0 when they initially sign up
    """
    serial = models.CharField(max_length=24, unique=True)
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    meetingsAttended = models.IntegerField(default=0)

class Meeting(models.Model):
    """
    Model for club meetings attended
    serial is from Rowan ID Card
    meetingDate is date and time of meeting attended
    """
    serial = models.CharField(max_length=24, unique=True)
    meetingDate = models.DateTimeField(default=datetime.now(), null=False)

class Committee(models.Model):
    """
    Model for committees
    serial is from Rowan ID card
    committeeName is the name of committee within the club
    """
    serial = models.CharField(max_length=24, unique=True)
    committeeName = models.CharField(max_length=32)



