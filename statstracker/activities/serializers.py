__author__ = 'trippshealy'

from rest_framework import serializers
from .models import Activities, Date
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.fields import SerializerMethodField


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date