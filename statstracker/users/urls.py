"""mowdie URL Configuration

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
from django.conf.urls import url
from users import views as users_views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^register/$', users_views.user_register, name="view_register"),
    # url(r'^edit/', users_views.edit_profile, name="view_profile"),
    url(r'^login/$',  'django.contrib.auth.views.login',  name='view_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='view_logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^accounts/profile', RedirectView.as_view(
                                pattern_name='view_index'
                                ), name='view_profile')
    # url(r'^accounts/profile', users_views.user_dashboard, name='dashboard'),
]
