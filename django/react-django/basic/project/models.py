from django.db import models

# Create your models here.
class User(models.Model):
      name = models.CharField(max_length=100)
      email = models.CharField(max_length=100,unique=True)
      password = models.CharField(max_length=100,unique=True)
      created_at=models.DateTimeField(auto_now_add=True)