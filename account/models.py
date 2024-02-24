from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)