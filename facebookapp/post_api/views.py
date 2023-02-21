from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer

# Get news feed: GET /api/posts/news-feed/
# Create post for news feed: POST /api/posts/news-feed/
# Get group posts: GET /api/posts/groups/{group_id}/
# Create post for group: POST /api/posts/groups/{group_id}/
# Get post details: GET /api/posts/{post_id}/
# Like post: POST /api/posts/{post_id}/like/
# Get post likes: GET /api/posts/{post_id}/likes/
# Create post comment: POST /api/posts/{post_id}/comments/
# Get post comments: GET /api/posts/{post_id}/comments/

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/posts/news-feed/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
        {
            'Endpoint': '/posts/news-feed/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/posts/groups/id/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
        {
            'Endpoint': '/posts/groups/id/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/posts/id',
            'method': 'GET',
            'body': None,
            'description': ''
        },
        {
            'Endpoint': '/posts/id/reactions/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/posts/id/reactions/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
        {
            'Endpoint': '/posts/id/comments/',
            'method': 'POST',
            'body': {'body': ""},
            'description': ''
        },
        {
            'Endpoint': '/posts/id/comments/',
            'method': 'GET',
            'body': None,
            'description': ''
        },
    ]
    return Response(routes)