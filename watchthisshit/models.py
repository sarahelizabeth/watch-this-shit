from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def get_user_if_deleted():
    return User.objects.get_or_create(username="[user deleted]")[0]

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
    
def get_media_type():
    return MediaType.objects.get_or_create(name="Media")[0]

def get_media_type_id():
    return get_media_type().id
    
class MediaType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
def get_recommendation():
    return Recommendation.objects.get_or_create(title="[rec deleted]")[0]

def get_recommendation_id():
    return get_recommendation().id

class Recommendation(models.Model):
    user = models.ForeignKey(
        User, related_name="recs", on_delete=models.SET(get_user_if_deleted)
    )
    recipients = models.ManyToManyField(
        Profile, related_name="received_recs", symmetrical=False, blank=True
    )
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    media_type = models.ForeignKey(
        MediaType, on_delete=models.SET(get_media_type), default=get_media_type_id
    )
    genres = models.ManyToManyField(
        Genre, related_name="genres", symmetrical=False, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%y-%m-%d %H:%M}): "
            f"{self.title}"
        )
    
class Comment(models.Model):
    recommendation: models.ForeignKey(
        Recommendation, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
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