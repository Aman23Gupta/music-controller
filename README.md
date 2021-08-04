## music-controller

### A co-oprative app where group of people can join and lisiten music 
### Music is handle by group admin

```
>> dependancies
pip install django djangorestframework

>> to start project
django-admin startproject music_controller
django-admin startapp api
```

```python

>> music_controller/settings.py

INSTALLED_APPS = []  // add

'api.apps.ApiConfig', //your app
'rest_framework'

>> views.py #this where we write all our endpoint (location on web sever that we are going to)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("Hello")

# Create your views here.

>> music_controller/urls.py

"""music_controller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include('api.urls'))
]


>> api/urls.py

from django.conf.urls import url
from .views import main

urlpatterns = [
    url(r'^home/',main)
]

```

```
>> to start a server

python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py runserver
```

### frontend dependancies
```
django-admin startapp frontend
npm init -y
npm i webpack webpack-cli --save-dev
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
npm install @material-ui/core
npm install @babel/plugin-proposal-class-properties
npm install react-router-dom
npm install @material-ui/icons
```