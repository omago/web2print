#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('press.backend_views',
    url(r'^admin/press/form/(?P<pk>.*)', 'form', name="admin-press-form"),
    url(r'^admin/press/form', 'form', name="admin-press-form"),
    url(r'^admin/press/details/(?P<pk>.*)', 'details', name="admin-press-details"),
    url(r'^admin/press/delete/(?P<pk>.*)', 'delete', name="admin-press-delete"),
    url(r'^admin/press/list', 'list', name="admin-press-list"),
    url(r'^admin/press', 'index', name="admin-press-index"),
)