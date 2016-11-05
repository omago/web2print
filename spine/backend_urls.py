#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('spine.backend_views',
    url(r'^admin/spine/form/(?P<pk>.*)', 'form', name="admin-spine-form"),
    url(r'^admin/spine/form', 'form', name="admin-spine-form"),
    url(r'^admin/spine/details/(?P<pk>.*)', 'details', name="admin-spine-details"),
    url(r'^admin/spine/delete/(?P<pk>.*)', 'delete', name="admin-spine-delete"),
    url(r'^admin/spine/list', 'list', name="admin-spine-list"),
    url(r'^admin/spine', 'index', name="admin-spine-index"),
)