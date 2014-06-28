from django.db import models
from waiter.models import Waiter
from bartender.models import Bartender

# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=30, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)


class Sales(models.Model):
    item = models.ForeignKey(Stock, unique=True)
    count = models.IntegerField(max_length=2000, default=0)

    def __unicode__(self):
        return "%s     %s" % (self.item.name, self.count)


class StatusOrders(models.Model):
    items = models.CharField(max_length=30,
                             blank=False)
    amount = models.CharField(max_length=30, blank=False,
                              )
    date_and_time = models.DateTimeField(auto_now=True)
    STATUS = (
        ('W', 'Waiting'),
        ('A', 'Adopted'),
        ('R', 'Ready')
              )
    status = models.CharField(choices=STATUS, max_length=7)
    waiter = models.CharField(max_length=30, blank=False)
    bartender = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        try:
            existing = StatusOrders.objects.get(items=self.items)
            self.id = existing.id #force update instead of insert
        except StatusOrders.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)

    def __unicode__(self):
        return "%s %s" % (self.items, self.amount)

    def get_model_fields(self):
        return self._meta.fields




