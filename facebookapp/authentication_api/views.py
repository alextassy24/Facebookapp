from django.http import response
from django.core.exceptions import ValidationError
from django.db import IntegrityError, DatabaseError
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework.authtoken.models import Token
from .models import NewUser
from .serializers import NewUserSerializer

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
    email = request.data.get('email')
    password = request.data.get('password')
    serializer = NewUserSerializer(data=request.data)
    if serializer.is_valid() and not NewUser.objects.filter(email=email).exists():
        user = serializer.save(password=make_password(password))
        return Response({
            'status': 'Account created successfully!',
        })
    else:
        errors = {}
        for field, errors_list in serializer.errors.items():
            errors[field] = errors_list[0]
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)  
    
@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({'status': 'Email and password are required.'}, status=400)
    #de verificat parola cu hashing, si daca corespunde emailul
    user = authenticate(request=request, username=email, password=password)
    
    if not user:
        return Response({'status': 'Invalid email or password.'}, status=401)
    if request.user.is_authenticated:
        return Response({'status': 'User is already logged in.'})
    login(request, user)
    return Response({'status': 'Login successful.'})

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'status': 'Logged out successfully!'})