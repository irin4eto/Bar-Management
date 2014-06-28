from django.db import models
from django.contrib.auth.models import User


class Manager(models.Model):
    manager = models.ForeignKey(User, unique=True)

    def save(self, *args, **kwargs):
        try:
            existing = Manager.objects.get(manager=self.manager)
            self.id = existing.id #force update instead of insert
        except Manager.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)

    def __unicode__(self):
        return self.manager.username
