from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from .models import Activities, Stats
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from users.models import Profile
from .serializers import ActivitiesSerializer, StatsSerializer
from rest_framework.response import Response
from rest_framework import generics

class ActivitiesViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitiesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Activities.objects.filter(profile__user=self.request.user)

    def perform_create(self, serializer):
        prof = self.request.user.profile
        serializer.save(profile=prof)



class StatsViewSet(viewsets.ModelViewSet):
    serializer_class = StatsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Stats.objects.filter(activities__profile__user = self.request.user)



class StatsList(generics.ListCreateAPIView):
    # queryset = Stats.objects.all()
    serializer_class = StatsSerializer

    def get_queryset(self):
        activitypk = self.kwargs['pk']
        return Stats.objects.filter(activities__pk=activitypk)


class StatsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    serializer_class = StatsSerializer

    def get_queryset(self):
        statspk = self.kwargs['pk']
        return Stats.objects.filter(stats__pk=statspk)
