"""mysite URL Configuration

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
from django.urls import path
from mysite.views import current_datetime
from django.conf.urls.defaults import *

urlpatterns = ['',
    path('admin/', admin.site.urls),
    path(r'^time/$', current_datetime),
]

# urlpatterns = patterns('',
# Example:
# (r'^mysite/', include('mysite.apps.foo.urls.foo')),
# Uncomment this for admin:
# (r'^admin/', include('django.contrib.admin.urls')),
# )