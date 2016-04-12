from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import admin, user

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from models import Member, Meetings

from serializers import MemberSerializer, MeetingsSerializer

# Create Your Views Here

class JSONResponse(HttpResponse):
    """ JSONResponse Extends HttpResponse
    This allows us to send JSON to a browser
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class MemberViewSet(viewsets.ModelViewSet):
    """ Extends ModelViewSet from rest_framework
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-date_joined')
    serializer_class = MemberSerializer
    def list_members(request):
        if admin:
            if request.method == 'GET':
                members = Member.objects.all()
                serializer = MemberSerializer(members, many=True)
                return JSONResponse(serializer.data)
	    else:
	        return HttpResponse(status=404)
	    return render("html", {})

	"""
	elif user:
	    if request.method == 'GET':
	        members = Member.objects.?
	
	    else:
	        return HttpResponse(status=404)
	else:
	    return HttpResponse(status=403)

	"""

    def post_member(self):
         if not self.body:
             return HttpResponse(status=400)
         try:
             members = Member()
         except:
             return HttpResponse(status=404)
         if self.method == 'POST':
             data = JSONParser().parse(self)
             if((not 'auth_token' in data) or auth_token != data['auth_token']):
                 return HttpResponse(status=401)
             else:
                 del data['auth_token']
                 serializer = MemberSerializer(members, data=data)
                 if serializer.is_valid():
                     serializer.save()
                     return JSONResponse(serializer.data, status=201)
                 return JSONResponse(serializer.errors, status=400)

class MeetingsViewSet(viewsets.ModelViewSet):
    """ Extends ModelViewSet from rest_framework
    Allows certain users to see which Meetings were attended (by date and time)
    Should list everything in the Meetings table
    """
    def listMembers(self):
       if self.method == 'GET':
           meetings = Meetings.objects.all()
           serializer = MeetingsSerializer(Meetings, many = True)
           return JSONResponse


       

