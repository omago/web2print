#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('finish.backend_views',
    url(r'^admin/finish/form/(?P<pk>.*)', 'form', name="admin-finish-form"),
    url(r'^admin/finish/form', 'form', name="admin-finish-form"),
    url(r'^admin/finish/details/(?P<pk>.*)', 'details', name="admin-finish-details"),
    url(r'^admin/finish/delete/(?P<pk>.*)', 'delete', name="admin-finish-delete"),
    url(r'^admin/finish/list', 'list', name="admin-finish-list"),
    url(r'^admin/finish', 'index', name="admin-finish-index"),
)