"""statstracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from activities import views as act_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"activities", act_views.ActivitiesViewSet, base_name='activities')
router.register(r"stats", act_views.StatsViewSet, base_name='stats')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='view_index'),
    url(r'^', include('users.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace ='rest_framework')),
    url(r'^api/activities/(?P<pk>\d+)/stats/$', act_views.StatsList.as_view(), name='stats-list'),
    url(r'^api/stats/(?P<pk>\d+)$', act_views.StatsDetailView.as_view(), name='stats-detail')
]
