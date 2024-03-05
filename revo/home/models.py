from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Signup(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

