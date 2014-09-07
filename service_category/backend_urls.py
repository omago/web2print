#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('service_category.backend_views',
    url(r'^admin/service-category/form/(?P<pk>.*)', 'form', name="admin-service-category-form"),
    url(r'^admin/service-category/form', 'form', name="admin-service-category-form"),
    url(r'^admin/service-category/details/(?P<pk>.*)', 'details', name="admin-service-category-details"),
    url(r'^admin/service-category/delete/(?P<pk>.*)', 'delete', name="admin-service-category-delete"),
    url(r'^admin/service-category/list', 'list', name="admin-service-category-list"),
    url(r'^admin/service-category', 'index', name="admin-service-category-index"),
)