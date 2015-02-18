#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('flexion.backend_views',
    url(r'^admin/flexion/form/(?P<pk>.*)', 'form', name="admin-flexion-form"),
    url(r'^admin/flexion/form', 'form', name="admin-flexion-form"),
    url(r'^admin/flexion/details/(?P<pk>.*)', 'details', name="admin-flexion-details"),
    url(r'^admin/flexion/delete/(?P<pk>.*)', 'delete', name="admin-flexion-delete"),
    url(r'^admin/flexion/list', 'list', name="admin-flexion-list"),
    url(r'^admin/flexion', 'index', name="admin-flexion-index"),
)