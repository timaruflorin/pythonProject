from django.contrib.auth.models import User
from django.db import models


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Users(MyModel):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=50)


class Offers(MyModel):
    title = models.CharField(max_length=150, unique=True)
    picture = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=1500, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
