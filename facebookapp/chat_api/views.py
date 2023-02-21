from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer

# Get chat rooms: GET /api/chat/rooms/
# Get chat room messages: GET /api/chat/rooms/{room_id}/messages/
# Send message to chat room: POST /api/chat/rooms/{room_id}/messages/
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/chat/rooms/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
        {
            'Endpoint': '/chat/rooms/id/messages/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
        {
            'Endpoint': '/chat/rooms/id/messages/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
    ]
    return Response(routes)