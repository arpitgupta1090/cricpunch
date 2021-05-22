from rest_framework.views import APIView
from rest_framework.response import Response
import api.utils


class ListSeries(APIView):
    def get(self, request):
        data = api.utils.all_series()
        return Response(data)


class GetSeries(APIView):
    def get(self, request, pk):
        data = api.utils.get_series(pk)
        return Response(data)


class GetMatch(APIView):
    def get(self, request, pk):
        data = api.utils.get_match(pk)
        return Response(data)
