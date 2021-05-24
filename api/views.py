from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

import api.utils as utils
from api.models import User
from api.serializers import UserSerializer


class ListSeries(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = utils.all_series()
        return Response(data)


class GetSeries(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        data = utils.get_series(pk)
        return Response(data)


class GetMatch(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        data = utils.get_match(pk)
        return Response(data)


class GetPlayers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        data = utils.get_players(pk)
        return Response(data)


class AllUrls(APIView):
    def get(self, request):
        data = utils.get_urls()
        return Response(data)


class Home(APIView):
    def get(self, request):
        data = {
            'signup/': 'sign-up for registering to get auth Token using valid email, name and password',
            'login/': 'login to obtain auth token',
            'api/': 'List of all urls. Please use token auth to use the this service',
        }
        return Response(data)


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


