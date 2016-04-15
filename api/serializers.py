from rest_framework import serializers

from models import Member
from models import Meetings
from models import Committees

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


class CommitteeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Committees
    """
    class Meta:
        model = CommitteeSerializer
        fields = ('id', 'serial', 'committeeName')
