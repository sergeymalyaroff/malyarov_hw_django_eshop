from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    email = models.EmailField(unique=True)


class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
