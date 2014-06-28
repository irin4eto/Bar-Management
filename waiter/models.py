from django.db import models
from django.contrib.auth.models import User


class Waiter(models.Model):
    waiter = models.ForeignKey(User, unique=True)

    def save(self, *args, **kwargs):
        try:
            existing = Waiter.objects.get(waiter=self.waiter)
            self.id = existing.id #force update instead of insert
        except Waiter.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)

    def __unicode__(self):
        return self.waiter.username
