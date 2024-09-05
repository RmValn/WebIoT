from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.

# class User(AbstractUser):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     username = models.CharField(max_length=30,unique=True)
#     email = models.EmailField(unique=True)
#     gender = models.CharField(max_length=20, choices=(('M', 'Male'), ('F', 'Female')))
#     joined_date = models.DateField(null=True)
    
#     def __str__(self): # this method returns the username as the name of the object instead of "object" when we fetch it's name in admin or in shell
#         return self.username 