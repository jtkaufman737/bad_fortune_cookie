from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from bad_fortune_cookie.fortunes.serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FortuneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to interact with fortunes
    """
    pagination_class = None
    queryset = Fortune.objects.all()
    serializer_class = FortuneSerializer
