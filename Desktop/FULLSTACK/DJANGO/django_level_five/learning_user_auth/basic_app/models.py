from django.contrib.auth.models import User
from django.db import models

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return self.user.username