from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# class UserManager(models.Model):
    # def get_queryset(self):
        # return super(UserManager, self).get_queryset().filter(information='testing')

class Licences(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'IN_PROGRESS'),
        ('finished', 'FINISHED'),
    )
    name = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    issued_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(default=timezone.now)
    licence_number = models.CharField(max_length=255, default=0)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Licences"
        ordering = ('expiry_date',)
