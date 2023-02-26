import json

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import send_on_start, send_to_nova, get_webhook_info, set_webhook


@swagger_auto_schema(method='post', responses={200: ''})
@api_view(['POST', ])
def api_webhook(request):
    response = json.loads(request.body)
    print(response)
    if 'text' in response['message']:
        if response['message']['text'] == '/start':
            send_on_start.delay(response['message']['chat']['id'])
    if 'contact' in response['message']:
        send_to_nova.delay(response['message']['contact']['phone_number'], response['message']['chat']['username'])
    return Response(status=status.HTTP_200_OK)


@swagger_auto_schema(method='get', responses={200: ''})
@api_view(['GET', ])
def api_set_webhook(request):
    return Response(set_webhook(), status=status.HTTP_200_OK)


@swagger_auto_schema(method='get', responses={200: ''})
@api_view(['GET', ])
def api_get_webhook_info(request):
    return Response(get_webhook_info(), status=status.HTTP_200_OK)
