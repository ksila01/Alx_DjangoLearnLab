# social_media_api/accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

def profile_upload_path(instance, filename):
    return f"profiles/{instance.username}/{filename}"

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=profile_upload_path, blank=True, null=True)
    # Explicit "following" relation (users I follow)
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True,
    )

    def __str__(self):
        return self.username

