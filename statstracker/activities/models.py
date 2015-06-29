from django.db import models
from users.models import Profile
from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone
import datetime

# Create your models here.

class Activities(models.Model):
    profile = models.ForeignKey(Profile)
    creation_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)


class Stats(models.Model):
    activities = models.ForeignKey(Activities)
    stat = models.IntegerField()
    date = models.DateField(default=datetime.date.today)




