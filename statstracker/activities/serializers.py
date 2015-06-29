__author__ = 'trippshealy'

from rest_framework import serializers
from .models import Activities, Stats
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.fields import SerializerMethodField


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats