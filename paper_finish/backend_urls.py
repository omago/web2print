#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('paper_finish.backend_views',
    url(r'^admin/paper-finish/form/(?P<pk>.*)', 'form', name="admin-paper-finish-form"),
    url(r'^admin/paper-finish/form', 'form', name="admin-paper-finish-form"),
    url(r'^admin/paper-finish/details/(?P<pk>.*)', 'details', name="admin-paper-finish-details"),
    url(r'^admin/paper-finish/delete/(?P<pk>.*)', 'delete', name="admin-paper-finish-delete"),
    url(r'^admin/paper-finish/list', 'list', name="admin-paper-finish-list"),
    url(r'^admin/paper-finish', 'index', name="admin-paper-finish-index"),
)