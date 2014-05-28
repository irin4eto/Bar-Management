from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserManager(BaseUserManager):
    STAFF = ('MANAGER', 'WAITER', 'BARTENDER')

    def create_user(self, role, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not role in UserManager.STAFF:
            raise ValueError("Wrong role")

        user = self.model(
            role=role, email=UserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, role, email, password):
            user = self.create_user(email, password=password, role=role)
            user.is_admin = True
            user.save(using=self._db)
            return user


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField(blank=False, max_length=30)
    role = models.CharField(blank=False, max_length=9)
    first_name = models.CharField(blank=False, max_length=30)
    last_name = models.CharField(blank=False, max_length=30)

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)




