from django.db import models
from django.contrib.auth.models import User

from django.utils.datetime_safe import datetime


class Bicycle(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    note = models.TextField()
    owner = models.ForeignKey(User)
    city = models.CharField(max_length=50, blank = True)
    serial_number = models.CharField(max_length=50, blank=True)
    registration_date = models.DateTimeField('Date registered', default=datetime.now)
    is_stolen = models.BooleanField(default=False)

    def __str__(self):
        return "%s's %s %s %s" % (self.owner, self.year, self.brand, self.model)


class BicyclePhoto(models.Model):
    bicycle = models.ForeignKey(Bicycle)
    image = models.ImageField()