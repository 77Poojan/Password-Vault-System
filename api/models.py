from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserVault(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
 
    def __str__(self):
        return self.name