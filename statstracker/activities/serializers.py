__author__ = 'trippshealy'

from rest_framework import serializers
from .models import Activities, Stats
from users.models import Profile
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.fields import SerializerMethodField


class ActivitiesSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    creation_date = serializers.IntegerField
    title = serializers.CharField(max_length=255)
    stats = serializers.HyperlinkedIdentityField(view_name='stats-list')

    class Meta:
        model = Activities

        fields = ('id', 'profile', 'title', 'profile', 'creation_date', 'stats')


class StatsSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(read_only=True)
    date = serializers.DateField(input_formats=['%Y-%m-%d'])
    #input_formats=['%d/%m/%Y']) # YYYY[-MM[-DD]] # format=['iso-8601']

    class Meta:
        model = Stats
