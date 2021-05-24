from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

import api.utils as utils
from api.models import User
from api.serializers import UserSerializer


class ListSeries(APIView):
    def get(self, request):
        data = utils.all_series()
        return Response(data)


class GetSeries(APIView):
    def get(self, request, pk):
        data = utils.get_series(pk)
        return Response(data)


class GetMatch(APIView):
    def get(self, request, pk):
        data = utils.get_match(pk)
        return Response(data)


class GetPlayers(APIView):
    def get(self, request, pk):
        data = utils.get_players(pk)
        return Response(data)


class AllUrls(APIView):
    def get(self, request):
        data = utils.get_urls()
        return Response(data)


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


