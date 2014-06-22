from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
# Create your models here.


class UserManager(BaseUserManager):
    STAFF = ('MANAGER', 'WAITER', 'BARTENDER')

    """def create_user(self, role, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not role in UserManager.STAFF:
            raise ValueError("Wrong role")

        user = self.model(
            role=role, email=UserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user"""

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


    def save(self, *args, **kwargs):
        try:
            existing = UserProfile.objects.get(user=self.user)
            self.id = existing.id #force update instead of insert
        except UserProfile.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)


    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

"""post_save.connect(create_user_profile, sender=User)"""




