from rest_framework.serializers import ModelSerializer
from .models import NewUser

class NewUserSerializer(ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id','first_name', 'last_name','email','phone_number','date_joined']
        