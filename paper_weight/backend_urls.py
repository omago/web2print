#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('paper_weight.backend_views',
    url(r'^admin/paper-weight/form/(?P<pk>.*)', 'form', name="admin-paper-weight-form"),
    url(r'^admin/paper-weight/form', 'form', name="admin-paper-weight-form"),
    url(r'^admin/paper-weight/details/(?P<pk>.*)', 'details', name="admin-paper-weight-details"),
    url(r'^admin/paper-weight/delete/(?P<pk>.*)', 'delete', name="admin-paper-weight-delete"),
    url(r'^admin/paper-weight/list', 'list', name="admin-paper-weight-list"),
    url(r'^admin/paper-weight', 'index', name="admin-paper-weight-index"),
)