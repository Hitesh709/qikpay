
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    total_spent = models.FloatField(default=0)
    points = models.IntegerField(default=0)
    crypto_tokens = models.IntegerField(default=0)
