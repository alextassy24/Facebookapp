from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import Serializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
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
@permission_classes([AllowAny])
def register(request):
    serializer = NewUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        print("Serializer Errors:", serializer.errors)
        errors = serializer.errors
        if 'email' in errors:
            email_errors = errors['email']
            if 'A user with that email already exists.' in email_errors:
                return Response({'detail': 'A user with that email already exists.'}, status=400)
        return Response(errors, status=400)

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'status': 'Email and password are required.'}, status=400)

    user = authenticate(request=request, email=email, password=password, backend='authentication_api.views.EmailBackend')

    if not user:
        return Response({'status': 'Invalid email or password.'}, status=401)

    if request.user.is_authenticated:
        return Response({'status': 'User is already logged in.'})

    login(request, user, backend='authentication_api.views.EmailBackend')
    return Response({'status': 'Login successful.'})

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'status': 'Logged out successfully!'})