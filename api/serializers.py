from rest_framework import serializers

<<<<<<< HEAD
=======

>>>>>>> f986dd158f6425084296b38923cdb173b25f7e64
from models import Member
from rest_framework import serializers


class MemberSerializer(serializers.HyperlinkedModelSerializer):
<<<<<<< HEAD
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'meeting_attend')

=======
	class Meta:
            	model = Member
		fields = ('id', 'first_name', 'last_name', 'meeting_attend')
>>>>>>> f986dd158f6425084296b38923cdb173b25f7e64
