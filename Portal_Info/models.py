from msilib.schema import Class
from pyexpat import model
from django.db import models

# Create your models here.

class PortalPage(models.Model):
    StdInfo=models.TextField(max_length=200)
    StdName=models.CharField(max_length=50)
    StdID=models.IntegerField
    StdSelection=models.IntegerField

class PortalInformation(models.Model):
    Homepage=models.TextField(max_length=200)
