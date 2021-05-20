from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Profile

'''
@receiver(post_save, sender=User) #when a user is saved, send  signal to this receiver, this receiver is the create profile function which takes all of these arguments
def CreateProfile(sender, instance, created, **kwargs): #the function therefore creates a profile object if the created object exists
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #
def SaveProfile(sender, instance, **kwargs):
    instance.profile.save()

'''