from rest_framework import serializers

from models import Member, Meeting, Committee

# Create Your Serializers Here

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for member Model
    """
    class Meta:
        model = Member
        fields = ('id', 'serial', 'firstName', 'lastName', 'meetingsAttended')

class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Meetings Model
    """
    class Meta:
        model = Meeting
        fields = ('id', 'serial', 'meetingDate')


class CommitteeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Committees Model
    """
    class Meta:
        model = Committee
        fields = ('id', 'serial', 'committeeName')
