from django.db import models

# Create your models here.

class Signup(models.Model):
    # id= models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=254,blank=True, null=True )
    password=models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



