#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('banner.backend_views',
    url(r'^admin/banner/form/(?P<pk>.*)', 'form', name="admin-banner-form"),
    url(r'^admin/banner/form', 'form', name="admin-banner-form"),
    url(r'^admin/banner/details/(?P<pk>.*)', 'details', name="admin-banner-details"),
    url(r'^admin/banner/delete/(?P<pk>.*)', 'delete', name="admin-banner-delete"),
    url(r'^admin/banner/list', 'list', name="admin-banner-list"),
    url(r'^admin/banner', 'index', name="admin-banner-index"),
)