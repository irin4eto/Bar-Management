from django.db import models
from django.contrib.auth.models import User


class Bartender(models.Model):
    bartender = models.ForeignKey(User, unique=True)

    def save(self, *args, **kwargs):
        try:
            existing = Bartender.objects.get(bartender=self.bartender)
            self.id = existing.id #force update instead of insert
        except Bartender.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)

    def __unicode__(self):
        return self.bartender.username
