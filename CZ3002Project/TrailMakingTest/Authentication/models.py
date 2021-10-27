from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    age = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Attempts(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True, blank=True)
    timeToComplete = models.FloatField(null=True)
    numOfErrors = models.IntegerField(null=True)
    errorPerSec = models.FloatField(null=True)
    errorPencentage = models.FloatField(null=True)




