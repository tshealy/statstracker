from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from .models import Activities, Stats
from rest_framework.exceptions import PermissionDenied
import django_filters
from django.contrib.auth.models import User
from .users import Profile
from .serializers import ActivitiesSerializer, StatsSerializer


class ActivitiesViewSet(viewsets.ModelViewSet):
    # queryset= Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #these need fixing
    def get_queryset(self):
        try:
            # profile = Profile.objects.get(id = self.kwargs['pk'])
            # return Activities.objects.filter(user_id = profile.id)
            return Activities.objects.filter(user = self.request.user)
        except:
            return "Object not found"


class StatsViewSet(viewsets.ModelViewSet):
    # queryset= Date.objects.all()
    serializer_class = StatsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #these need fixing
    def get_queryset(self):
        try:
            # profile = Profile.objects.get(id = self.kwargs['pk'])
            # return Stats.objects.filter(user_id = profile.id)
            return Stats.objects.filter(user = self.request.user)
        except:
            return "Object not found"