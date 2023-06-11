from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField( 
        'self',
        related_name='followed_by',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.user.username
    
class Recommendation(models.Model):
    user = models.ForeignKey(
        User, related_name="recs", on_delete=models.DO_NOTHING
    )
    recipients = models.ManyToManyField(
        Profile, related_name="received_recs", symmetrical=False, blank=True
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%y-%m-%d %H:%M}): "
            f"{self.title}"
        )
    
# Note: Django documentation mentions that the best place 
# to put your signals is in a new signals.py submodule of 
# your app. However, this requires you to make additional 
# changes in your app configuration. Since you only need 
# to build out a single signal for this tutorial, you’re 
# keeping it in models.py.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()