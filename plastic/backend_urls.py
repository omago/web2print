#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('plastic.backend_views',
    url(r'^admin/plastic/form/(?P<pk>.*)', 'form', name="admin-plastic-form"),
    url(r'^admin/plastic/form', 'form', name="admin-plastic-form"),
    url(r'^admin/plastic/details/(?P<pk>.*)', 'details', name="admin-plastic-details"),
    url(r'^admin/plastic/delete/(?P<pk>.*)', 'delete', name="admin-plastic-delete"),
    url(r'^admin/plastic/list', 'list', name="admin-plastic-list"),
    url(r'^admin/plastic', 'index', name="admin-plastic-index"),
)