from django.db.models.signals import post_save
from  django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.models import Group


# @receiver(post_save, sender=User)
# def CreateProfile(sender, instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user = instance)
#         print('Profile Created')

# #post_save.connect(CreateProfile, sender=User)

# @receiver(post_save, sender=User)
# def UpdateProfile(sender, instance,created,**kwargs):
#     if created == False:
#         instance.profile.save()
#         print("Profile updated")

#post_save.connect(UpdateProfile, sender=User)

def UserProfile(sender,instance,created, **kwargs):
    if created:
        group = Group.objects.get(name='Profile')
        instance.groups.add(group)
        Profile.objects.create(
            user=instance,
            )
        print("profile created successfully")
    instance.profile.save()
post_save.connect(UserProfile, sender=User)