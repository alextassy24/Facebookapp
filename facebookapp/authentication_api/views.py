from django.http import response
from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import NewUser
from .serializers import NewUserSerializer

# Register: POST /api/auth/register/
# Login: POST /api/auth/login/
# Logout: POST /api/auth/logout/
    
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/auth/register/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/auth/login/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/auth/logout/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
    ]
    return Response(routes)

@api_view(['POST'])
def register(request):
    serializer = NewUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'status': 'success',
            'user_id': user.id,
        })
    else:
        errors = {}
        for field, errors_list in serializer.errors.items():
            errors[field] = errors_list[0]
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['POST'])
def login(request):
    pass

@api_view(['POST'])
def logout(request):
    pass