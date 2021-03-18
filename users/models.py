from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField()
    avatar = models.ImageField()


class Customer(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)


class Courier(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    phone = models.IntegerField()







