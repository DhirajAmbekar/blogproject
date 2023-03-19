from django.db import models

# Create your models here.

class Owner(models.Model):
    username = models.CharField(max_length=50)  
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)  
    password = models.CharField( max_length=50,null= True,blank=True)

class Blogs(models.Model):
    name = models.CharField(max_length=50)  
    title = models.CharField(max_length=50)  
    image = models.ImageField(upload_to="images/", null= True,blank=True)