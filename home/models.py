# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Members(models.Model):

    #__Members_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    ministry = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateTimeField(blank=True, null=True, default=timezone.now)
    anniversary = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Members_FIELDS__END

    class Meta:
        verbose_name        = _("Members")
        verbose_name_plural = _("Members")


class Governors(models.Model):

    #__Governors_FIELDS__
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    list = models.TextField(max_length=255, null=True, blank=True)

    #__Governors_FIELDS__END

    class Meta:
        verbose_name        = _("Governors")
        verbose_name_plural = _("Governors")



#__MODELS__END
