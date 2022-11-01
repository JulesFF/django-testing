from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from django.contrib.auth import signals, get_user_model


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    updated_datetime = models.DateTimeField(
        null=False,
        editable=False,
        default=timezone.now,
        verbose_name="Updated")
    def __str__(self):
        return self.user.get_username()

    def save(self, *args, **kwargs):
        self.updated_datetime = timezone.now()
        return super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

