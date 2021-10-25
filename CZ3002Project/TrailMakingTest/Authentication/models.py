from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    age = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

# @receiver(post_save, sender=User)
# def CreateProfile(sender, instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user = instance)
#         print('Profile Created')

# post_save.connect(CreateProfile, sender=User)

# @receiver(post_save, sender=User)
# def UpdateProfile(sender, instance,created,**kwargs):
#     if created == False:
#         instance.profile.save()
#         print("Profile updated")

# post_save.connect(UpdateProfile, sender=User)