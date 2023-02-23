from django.contrib.auth.backends import BaseBackend
from authentication_api.models import NewUser

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = NewUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except NewUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return NewUser.objects.get(pk=user_id)
        except NewUser.DoesNotExist:
            return None
