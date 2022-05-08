from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")

    class Meta:
        verbose_name="user"
        verbose_name_plural="user"