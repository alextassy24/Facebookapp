from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer

# Get user friends: GET /api/friends/
# Add friend: POST /api/friends/{user_id}/add/
# Remove friend: POST /api/friends/{user_id}/remove/
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/friends/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
        {
            'Endpoint': '/chat/friends/id/add/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/chat/friends/id/remove/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
    ]
    return Response(routes)