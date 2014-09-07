#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

base_url = ""
if settings.HAS_FRONTEND:
    base_url = "admin"

urlpatterns = patterns('core.views',
    url(r'^' + base_url + '/account/login$', 'account.login', name="admin-login"),
    url(r'^' + base_url + '/account/logout$', 'account.logout_user', name="admin-logout"),

    url(r'^' + base_url + '/user/form/(?P<pk>.*)/', 'users.form', name="admin-user-form"),
    url(r'^' + base_url + '/user/form/', 'users.form', name="admin-user-form"),
    url(r'^' + base_url + '/user/details/(?P<pk>.*)', 'users.details', name="admin-user-details"),
    url(r'^' + base_url + '/user/delete/(?P<pk>.*)/', 'users.delete', name="admin-user-delete"),
    url(r'^' + base_url + '/user/list', 'users.list', name="admin-user-list"),
    url(r'^' + base_url + '/user/', 'users.index', name="admin-user"),

    url(r'^' + base_url + '/access-denied/$', 'default.access_denied', name="admin-access-denied"),
    url(r'^' + base_url + '/$', 'default.index', name="admin-index")
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)