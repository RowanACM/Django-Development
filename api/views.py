from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import admin

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from models import Member, Meetings, Committees

from serializers import MemberSerializer, MeetingsSerializer, CommitteeSerializer

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
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    def list_members(self, request):
        """ Given The right credentials
        View data on members of our club
        ADMIN: see everything
        USER: only be able to see their own data
        ELSE: 403 Forbidden
        """
        if not request.body:
            return HttpResponse(status=403)
        elif request.method == 'GET':
            if admin:
                serializer = MemberSerializer(self.queryset, many=True)
                data = JSONRenderer().render(serializer.data)
                return render("__.html", data)
	    elif user:
	        return render("__.html", data)
	    else:
                return HttpResponse(status=403)
	else:
            return HttpResponse(status=403)

    def post_member(self, request):
         if not request.body:
             return HttpResponse(status=400)
         try:
             members = Member()
         except:
             return HttpResponse(status=500)
         if request.method == 'POST':
             data = JSONParser().parse(request)
             if((not 'auth_token' in data) or settings.AUTH_TOKEN != data['auth_token']):
                 return HttpResponse(status=401)
             else:
                 del data['auth_token']
                 serializer = MemberSerializer(members, data=data)
                 if serializer.is_valid():
                     serializer.save()
                     return JSONResponse(serializer.data, status=201)
                 return JSONResponse(serializer.errors, status=400)
        else:
            return HttpResponse(status=403)

class MeetingsViewSet(viewsets.ModelViewSet):
    """ Extends ModelViewSet from rest_framework
    Allows certain users to see which Meetings were attended (by date and time)
    Should list everything in the Meetings table
    """
    queryset = Meetings.objects.all()
    serializer_class = MeetingsSerializer
    def list_meetings(self, request):
        """ Given The right credentials
        View data on members of our club
        ADMIN: see everything
        USER: only be able to see their own data
        ELSE: 403 Forbidden
        """
        if not request.body:
            return HttpResponse(status=403)
        elif request.method == 'GET':
            if admin:
                serializer = MeetingsSerializer(self.queryset, many=True)
                data = JSONRenderer().render(serializer.data)
                return render("__.html", data)
	    elif user:
	        return render("__.html", data)
	    else:
                return HttpResponse(status=403)
	else:
            return HttpResponse(status=403)



class CommitteesViewSet(viewsets.ModelViewSet):
    """ Extends ModelViewSet from rest_framework
    Allows certain users to see his/her committee info
    Should list everything in the Committees table
    """
    queryset = Committees.objects.all()
    serializer_class = CommitteeSerializer
    def list_committees(self, request):
        """ Given The right credentials
        View data on members of our club
        ADMIN: see everything
        USER: only be able to see their own data
        ELSE: 403 Forbidden
        """
        if not request.body:
            return HttpResponse(status=403)
        elif request.method == 'GET':
            if admin:
                serializer = CommitteeSerializer(self.queryset, many=True)
                data = JSONRenderer().render(serializer.data)
                return render("__.html", data)
	    elif user:
	        return render("__.html", data)
	    else:
                return HttpResponse(status=403)
	else:
            return HttpResponse(status=403)

def increment_attendance(request):
    if not request.body:
        return HttpResponse(status=400)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if not ('auth_token' in data) or (settings.AUTH_TOKEN != data['auth_token']):
            return HttpResponse(status=401)
        else:
            del data['auth_token']
            try:
                meeting = Meeting()
            except:
                return HttpResponse(status=500)
            serializer = MeetingSerializer(meeting, data=data)
            if serializer.is_valid():
                try:
                    Member.objects.raw('UPDATE api_member SET meetings_attended = meetings_attended + 1 WHERE serial=' + data['serial'] + ';')
                except:
                    return HttpResponse(status=500)
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            else:
                return JSONResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=400)
                
        
