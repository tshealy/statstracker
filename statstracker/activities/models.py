from django.db import models
from statstracker.users import Profile
from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone

# Create your models here.

class Activities(models.Model):
    Profile = models.ForeignKey(Profile)
    created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True)

    #may need to show how many days we have done this
    # def total_day(self):
    #     return self.day_set.count()

class Date(models.Model):
    Activities = models.ForeignKey(Activities)
    day = models.DateTimeField(default=timezone.now)

