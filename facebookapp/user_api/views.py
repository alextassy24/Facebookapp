from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer

# Get user profile: GET /api/users/{user_id}/profile/
# Update user profile: PUT /api/users/{user_id}/profile/
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/users/id/profile/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/users/id/profile/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
    ]
    return Response(routes)