from django.db import models

# Create your models here.
class PatientInformation(models.Model):
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    race = models.CharField(max_length=100)
