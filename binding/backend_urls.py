#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('binding.backend_views',
    url(r'^admin/binding/form/(?P<pk>.*)', 'form', name="admin-binding-form"),
    url(r'^admin/binding/form', 'form', name="admin-binding-form"),
    url(r'^admin/binding/details/(?P<pk>.*)', 'details', name="admin-binding-details"),
    url(r'^admin/binding/delete/(?P<pk>.*)', 'delete', name="admin-binding-delete"),
    url(r'^admin/binding/list', 'list', name="admin-binding-list"),
    url(r'^admin/binding', 'index', name="admin-binding-index"),
)