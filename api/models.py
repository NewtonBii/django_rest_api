from django.db import models

# Create your models here.
# create a UserInformation class that will create new users
class UserInformation(models.Model):
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    race = models.CharField(max_length=100)
