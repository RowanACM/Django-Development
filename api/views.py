from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from models import Member
from models import Meetings

from serializers import MemberSerializer
from serializers import MeetingsSerializer

# Create Your Views Here

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-date_joined')
    serializer_class = MemberSerializer

"""
class MeetingsViewSet(viewsets.ModelViewSet):

   # Allows users to see which Meetings were attended (by date and time)
   # @Work-In Progress(WIP) TODO: Method should list everything in the Meetings table

    serializer_class = MeetingsSerializer
"""


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
