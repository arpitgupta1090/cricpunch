from rest_framework.views import APIView
from rest_framework.response import Response
import api.utils as utils


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
