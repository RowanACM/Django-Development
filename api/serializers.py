from rest_framework import serializers

from models import Member
from models import Meetings

# Create Your Serializers Here

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for member Model
    """
    class Meta:
        model = Member
        fields = ('id', 'serial', 'firstName', 'lastName', 'meetingsAttended')

class MeetingsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Mettings Model
    """
    class Meta:
        model = Meetings
        fields = ('id', 'serial', 'meetingDate')
