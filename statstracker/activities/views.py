from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, filters
from .models import Activities, Date
from rest_framework.exceptions import PermissionDenied
import django_filters
from django.contrib.auth.models import User
from .serializers import ActivitiesSerializer, DateSerializer


class ActivitiesViewSet(viewsets.ModelViewSet):
    # queryset= Activities.objects.all()
    serializer_class = ActivitiesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #these need fixing
    def get_queryset(self):
        try:
            activities = Activities.objects.get(id = self.kwargs['pk'])
            return Activities.objects.filter(user_id = activities.user.id)
        except:
            return "Object not found"


class DateViewSet(viewsets.ModelViewSet):
    # queryset= Date.objects.all()
    serializer_class = DateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #these need fixing
    def get_queryset(self):
        try:
            dates = Date.objects.get(id = self.kwargs['pk'])
            return Date.objects.filter(user_id = dates.user.id)
        except:
            return "Object not found"