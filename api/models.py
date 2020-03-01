from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from localflavor.us.models import USZipCodeField, USStateField
from phone_field import PhoneField

from api.constants import GENDER_CHOICES, PHONE_TYPE_CHOICES


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zipcode = USZipCodeField(null=True, blank=True)
    phone_number = PhoneField(null=True, blank=True)
    phone_type = models.CharField(max_length=10, choices=PHONE_TYPE_CHOICES, default='MOBILE')
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='MALE')
    passport_number = models.IntegerField(null=True, blank=True)
    passport_expiration = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    newsletter = models.BooleanField(default=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class LegacyUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zipcode = USZipCodeField(null=True, blank=True)
    phone_number = PhoneField(null=True, blank=True)
    phone_type = models.CharField(max_length=10, choices=PHONE_TYPE_CHOICES, default='MOBILE')
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='MALE')
    passport_number = models.IntegerField(null=True, blank=True)
    passport_expiration = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    newsletter = models.BooleanField(default=True)


class InterestedUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    newsletter = models.BooleanField(default=True)