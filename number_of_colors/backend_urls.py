#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('number_of_colors.backend_views',
    url(r'^admin/number-of-colors/form/(?P<pk>.*)', 'form', name="admin-number-of-colors-form"),
    url(r'^admin/number-of-colors/form', 'form', name="admin-number-of-colors-form"),
    url(r'^admin/number-of-colors/details/(?P<pk>.*)', 'details', name="admin-number-of-colors-details"),
    url(r'^admin/number-of-colors/delete/(?P<pk>.*)', 'delete', name="admin-number-of-colors-delete"),
    url(r'^admin/number-of-colors/list', 'list', name="admin-number-of-colors-list"),
    url(r'^admin/number-of-colors', 'index', name="admin-number-of-colors-index"),
)