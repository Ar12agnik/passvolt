from django.db import models
from django.contrib.auth.models import User
from passvolt.settings import key,chars
from .encription import encrypt,decrypt

# Create your models here.
class Password(models.Model):
    Url= models.URLField()
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    user_name = models.CharField(max_length=200,default=None)
    def save(self, *args, **kwargs):
       encrypted=encrypt(self.Password,key,chars)
       self.Password=encrypted
       super(Password, self).save(*args, **kwargs) # Call the real save() method
    def show(self):
        Password=self.Password
        decrypted=decrypt(Password,key,chars)
        return decrypted