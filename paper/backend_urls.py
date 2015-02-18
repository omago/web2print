#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('paper.backend_views',
    url(r'^admin/paper/form/(?P<pk>.*)', 'form', name="admin-paper-form"),
    url(r'^admin/paper/form', 'form', name="admin-paper-form"),
    url(r'^admin/paper/details/(?P<pk>.*)', 'details', name="admin-paper-details"),
    url(r'^admin/paper/delete/(?P<pk>.*)', 'delete', name="admin-paper-delete"),
    url(r'^admin/paper/list', 'list', name="admin-paper-list"),
    url(r'^admin/paper', 'index', name="admin-paper-index"),
)