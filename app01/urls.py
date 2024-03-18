#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import include
from django.urls import re_path as url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^send/sms/', views.send_sms),
    url(r'^register/', views.register, name='register'),  # "app01:register"
]
