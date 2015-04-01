#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('paper_type.backend_views',
    url(r'^admin/paper-type/form/(?P<pk>.*)', 'form', name="admin-paper-type-form"),
    url(r'^admin/paper-type/form', 'form', name="admin-paper-type-form"),
    url(r'^admin/paper-type/details/(?P<pk>.*)', 'details', name="admin-paper-type-details"),
    url(r'^admin/paper-type/delete/(?P<pk>.*)', 'delete', name="admin-paper-type-delete"),
    url(r'^admin/paper-type/list', 'list', name="admin-paper-type-list"),
    url(r'^admin/paper-type', 'index', name="admin-paper-type-index"),
)