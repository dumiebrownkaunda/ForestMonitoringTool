from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Areas(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Areas"


class Countries(models.Model):

    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    region = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.Countries

    class Meta:
        verbose_name_plural = "Countries"
