from django.urls import path, include
from .api import RegisterAPI, LoginAPI
from knox import views as knox_views
#from . import views

urlpatterns = [
    path('auth/', include('knox.urls')),
    path('auth/register/', RegisterAPI.as_view()),
    path('auth/login/', LoginAPI.as_view())
    
]

# urlpatterns = [
#     path('',views.getRoutes, name="routes"),
#     path('register/',views.register, name="register"),
#     path('login/',views.login_view, name="login-view"),
#     path('logout/',views.logout_view, name="logout-view"),
# ] 