from django.db import models

# Create your models here.
class User(models.Model):
    uname=models.CharField(max_length=20)
    uemail = models.EmailField()
    upassword = models.CharField(max_length=30)
    uconfirmpassword= models.CharField(max_length=30)
    uaddress= models.CharField(max_length=90)


