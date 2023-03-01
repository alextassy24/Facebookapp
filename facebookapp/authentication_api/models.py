from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, email, phone_number, first_name, last_name, date_of_birth, password=None, **kwargs):
        if not phone_number:
            raise ValueError("Phone number is required.")
        if not email:
            raise ValueError("Email is required.")
        if not password:
            raise ValueError("Password is required.")
        if not first_name:
            raise ValueError("First name is required.")
        if not last_name:
            raise ValueError("Last name is required.")
        if not date_of_birth:
            raise ValueError("Date of birth is required.")
        account = self.model(email=email, phone_number=phone_number, first_name=first_name,
                             last_name=last_name, date_of_birth=date_of_birth, **kwargs)
        account.set_password(password)
        account.save()
        return account


    def create_superuser(self, email, phone_number, first_name, last_name, date_of_birth, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        return self.create_user(email, phone_number, first_name, last_name, date_of_birth, password, **kwargs)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name', 'date_of_birth']

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.email}'
