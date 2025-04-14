from django.db import models

# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=100)
    money = models.IntegerField()
    Purchases = models.CharField(max_length=1000)
