from django.urls import path, include

api = [
    path('authentication_api/', include('authentication_api.urls')),
    path('chat_api/', include('chat_api.urls')),
    path('friend_api/', include('friend_api.urls')),
    path('group_api/', include('group_api.urls')),
    path('post_api/', include('post_api.urls')),
    path('user_api/', include('user_api.urls')),
]