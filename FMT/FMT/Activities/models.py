from django.db import models
from django.utils import timezone


# Create your models here.
class Activities(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'in_progress'),
        ('finished', 'finished'),
    )
    name = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    date_started = models.DateTimeField(default=timezone.now)
    closing_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
            verbose_name_plural = "Activities"


'''class Trips(models.Model):

        id = models.AutoField(primary_key=True)
        trip_id = models.IntegerField()
        date = models.DateField()
        retailer = models.CharField(max_length=50)
        brand = models.CharField(max_length=50)
        user_id = models.CharField(max_length=20)
        item_spend = models.IntegerField()
        item_units = models.IntegerField()

        def publish(self):
            self.save()

        def __str__(self):
            return str(self.id)'''


"""$ python manage.py shell

>>> from Activities.models import Activities
>>> Activities(name='pruning', amt=9).save()
>>> Activities(name='harvesting', amt=21).save()
>>> Activities(name='weeding', amt=15).save()
>>> Activities(name='planting', amt=12).save()
>>> Activities(name='thinning', amt=12).save()"""""
