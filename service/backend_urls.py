#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('service.backend_views',
    url(r'^admin/service/form/(?P<pk>.*)', 'form', name="admin-service-form"),
    url(r'^admin/service/form', 'form', name="admin-service-form"),
    url(r'^admin/service/details/(?P<pk>.*)', 'details', name="admin-service-details"),
    url(r'^admin/service/delete/(?P<pk>.*)', 'delete', name="admin-service-delete"),
    url(r'^admin/service/list', 'list', name="admin-service-list"),
    url(r'^admin/service', 'index', name="admin-service-index"),
)