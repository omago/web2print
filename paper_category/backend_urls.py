#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('paper_category.backend_views',
    url(r'^admin/paper-category/form/(?P<pk>.*)', 'form', name="admin-paper-category-form"),
    url(r'^admin/paper-category/form', 'form', name="admin-paper-category-form"),
    url(r'^admin/paper-category/details/(?P<pk>.*)', 'details', name="admin-paper-category-details"),
    url(r'^admin/paper-category/delete/(?P<pk>.*)', 'delete', name="admin-paper-category-delete"),
    url(r'^admin/paper-category/list', 'list', name="admin-paper-category-list"),
    url(r'^admin/paper-category', 'index', name="admin-paper-category-index"),
)