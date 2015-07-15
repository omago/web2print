#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('format.backend_views',
    url(r'^admin/format/form/(?P<pk>.*)', 'form', name="admin-format-form"),
    url(r'^admin/format/form', 'form', name="admin-format-form"),
    url(r'^admin/format/details/(?P<pk>.*)', 'details', name="admin-format-details"),
    url(r'^admin/format/delete/(?P<pk>.*)', 'delete', name="admin-format-delete"),
    url(r'^admin/format/list', 'list', name="admin-format-list"),
    url(r'^admin/format', 'index', name="admin-format-index"),
)