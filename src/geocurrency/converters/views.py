from django.http import HttpResponseNotFound
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BaseConverter, Batch
from .serializers import BatchSerializer


class WatchView(APIView):

    @swagger_auto_schema(responses={200: BatchSerializer})
    @action(['GET'], detail=True, url_path='', url_name="watch")
    def get(self, request, converter_id, *args, **kwargs):
        try:
            converter = BaseConverter.load(converter_id)
        except KeyError:
            return HttpResponseNotFound('Converter not found')
        batch = Batch(converter_id, converter.status)
        serializer = BatchSerializer(batch)
        return Response(serializer.data, content_type="application/json")
