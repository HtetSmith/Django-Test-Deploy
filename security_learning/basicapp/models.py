from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)
    #DONT FORGET TO INSTALL (PIP INSTALL PILLOW)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "User Informations"  # Change this to your desired display name
