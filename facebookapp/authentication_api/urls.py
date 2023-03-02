from django.urls import path, include
from .api import RegisterAPI, LoginAPI, TokenAPI
#from . import views

urlpatterns = [
    path('auth/register/', RegisterAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth/token/', TokenAPI.as_view())  
]

# urlpatterns = [
#     path('',views.getRoutes, name="routes"),
#     path('register/',views.register, name="register"),
#     path('login/',views.login_view, name="login-view"),
#     path('logout/',views.logout_view, name="logout-view"),
# ] 