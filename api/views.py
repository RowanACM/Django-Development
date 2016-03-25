from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from models import Member, Meetings

from serializers import MemberSerializer, MeetingsSerializer

# Create Your Views Here

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-date_joined')
    serializer_class = MemberSerializer
    def list_members(self):
        if self.method == 'GET':
            members = Member.objects.all()
            serializer = MemberSerializer(members, many=True)
            return JSONResponse(serializer.data)

class MeetingsViewSet(viewsets.ModelViewSet):
    Allows certain users to see which Meetings were attended (by date and time)
    should list everything in the Meetings table
    def listMembers(self):
       if self.method == 'GET':
           meetings = Meetings.objects.all()
           serializer = MeetingsSerializer(Meetings, many = True)
           return JSONResponse
