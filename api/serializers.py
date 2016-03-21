from rest_framework import serializers

from models import Member

# Create Your Serializers Here

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'meeting_attend')

