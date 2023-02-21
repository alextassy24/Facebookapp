from djongo import models

# Create your models here.
class NewUser(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_joined = models.DateField(auto_now_add=True)