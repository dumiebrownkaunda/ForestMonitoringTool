from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    year = models.IntegerField(default=0)


