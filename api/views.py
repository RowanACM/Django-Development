from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from models import Member
from rest_framework import viewsets
from serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-date_joined')
    serializer_class = MemberSerializer
=======
    	"""
        API endpoint that allows users to be viewed or edited.
	"""
	serializer_class = MemberSerializer
>>>>>>> f986dd158f6425084296b38923cdb173b25f7e64
