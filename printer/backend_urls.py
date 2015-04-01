#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('printer.backend_views',
    url(r'^admin/printer/form/(?P<pk>.*)', 'form', name="admin-printer-form"),
    url(r'^admin/printer/form', 'form', name="admin-printer-form"),
    url(r'^admin/printer/details/(?P<pk>.*)', 'details', name="admin-printer-details"),
    url(r'^admin/printer/delete/(?P<pk>.*)', 'delete', name="admin-printer-delete"),
    url(r'^admin/printer/list', 'list', name="admin-printer-list"),
    url(r'^admin/printer', 'index', name="admin-printer-index"),
)