from django.contrib.auth.hashers import check_password as auth_check_password
from djongo import models

class NewUser(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_joined = models.DateField(auto_now_add=True)

    def check_password(self, password):
        return auth_check_password(password, self.password)