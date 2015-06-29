from django.db import models

# from Mowdie
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Django-specific date and time handling
from django.utils import timezone
import datetime
import pytz

# Create your models here.
class Profile(models.Model):
	creation_date = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User)

	def __str__(self):
		return str(self.user)
