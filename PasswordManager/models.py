from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Password(models.Model):
    Url= models.URLField()
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    user_name = models.CharField(max_length=200,default=None)