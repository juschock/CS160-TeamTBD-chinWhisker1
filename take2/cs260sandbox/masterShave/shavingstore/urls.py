#!/usr/bin/env python3
"""shavingstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from shavingstore.shaver_mgt import views as shaver_views
# For debugging purposes
from django.conf import settings
from shavingstore.cart import views as cart_views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', shaver_views.fetch_all_shavers),
    url(r'^payment/', include('shavingstore.payment.urls',namespace="payment_ns")),
    url(r'^events/', include('shavingstore.events.urls',namespace="events_ns")),
    url(r'^shaver_mgt/', include('shavingstore.shaver_mgt.urls',namespace="shaver_mgt_ns")),
    url(r'^cart/$',cart_views.cart),
]
'''
if settings.DEBUG:
    #import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
'''
