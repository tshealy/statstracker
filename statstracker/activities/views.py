from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from .models import Activities, Stats
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from users.models import Profile
from .serializers import ActivitiesSerializer, StatsSerializer


class ActivitiesViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitiesSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Activities.objects.filter(profile__user=self.request.user)



class StatsViewSet(viewsets.ModelViewSet):
    serializer_class = StatsSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Stats.objects.filter(activities__profile__user = self.request.user)
