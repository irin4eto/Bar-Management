from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
# Create your models here.


class UserManager(BaseUserManager):
    STAFF = ('MANAGER', 'WAITER', 'BARTENDER')


    def create_superuser(self, role, email, password):
            user = self.create_user(email, password=password, role=role)
            user.is_admin = True
            user.save(using=self._db)
            return user


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    ROLE = (
        ('M', 'MANAGER'),
        ('W', 'WAITER'),
        ('B', 'BARTENDER')
    )
    role = models.CharField(choices=ROLE, max_length=9)
    objects = UserManager()

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)





