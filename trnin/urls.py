"""trnin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from user import views
import course.views

from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='Home'),
    path('register',views.register,name='register'),
    path('',include('django.contrib.auth.urls')),
    path('index',views.index),
    path('profile/',views.view_profile,name='profile'),
    path('profile/password/',views.change_password,name='change_password'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    url(r'^contact/$',course.views.contact, name='contact'),
    path('blog/',course.views.blog,name='blog'),
    url(r'^(?P<id>\d+)/$',course.views.coursedesc,name='detail'),
    url(r'^coursehome/(?P<courseid>[-\w]+)/$',course.views.coursehome,name='coursehome'),
    url(r'^coursecontent/(?P<courseid>[-\w]+)/$',course.views.coursec,name='coursecontent'),

    path('termsofservice/',course.views.termsofservice,name='termsofservice'),
    path('about/',course.views.about,name='about'),
    url(r'^requirements/(?P<courseid>[-\w]+)/$',course.views.requirements,name='requirements'),
    url(r'^schedules/(?P<courseid>[-\w]+)/$',course.views.schedules,name='schedules'),
    url(r'^exam/(?P<courseid>[-\w]+)/$',course.views.exam,name='exam'),
    url(r'^progress/(?P<courseid>[-\w]+)/$',course.views.progress,name='progress'),
    url(r'^add_question/(?P<courseid>[-\w]+)/$',course.views.add_question,name='add_question'),


    # url(r'^service/$',course.views.service, name='service'),

    # path('^',include('django.contrib.auth.urls'))

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
