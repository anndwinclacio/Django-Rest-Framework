# Where signals communications take place

from django.contrib.auth.models import User         
from django.db.models.signals import post_save      # used to send signal from a user model every time a user instance is saved
from django.dispatch import receiver                # used to receive this signal; check if it is created or updated

from profiles.models import Profile

# Function that is incharged in creating a new profile instance
@receiver(post_save, sender=User)                   # it has to accept a signal
def create_profile(sender, instance, created, **kwargs):
 #   print("Created: ", created)
    if created:
        Profile.objects.create(user=instance)

