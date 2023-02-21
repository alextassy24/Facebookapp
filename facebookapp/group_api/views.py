from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer

# Get user groups: GET /api/groups/
# Create group: POST /api/groups/
# Get group details: GET /api/groups/{group_id}/
# Join group: POST /api/groups/{group_id}/join/
# Leave group: POST /api/groups/{group_id}/leave/
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/groups/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
        {
            'Endpoint': '/groups/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/groups/id/',
            'method': 'GET',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/groups/id/join/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/groups/id/leave',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
    ]
    return Response(routes)