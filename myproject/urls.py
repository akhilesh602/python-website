"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello/',hello),
    path('hi/',hi),
    path('mygoogle/',mygoogle),
    path('welcome/<str:name>',welcome),
    path('index/',index),
    path('agra/',agra),
    path('forminput/',forminput),
    path('login/',login),
    path('success/',success),
    path('failed/',failed),
    path('stinput/',stinput),
    path('stsave/',stsave),
    path('stshow/',stshow),
    path('stfind/',stfind),
    path('searchdata/',searchdata),
    path('stdel/',stdel),
    path('deletedata/',deletedata),
    path('revised/',revised),
    path('python/',python),
]
