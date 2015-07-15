#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('insert_price.backend_views',
    url(r'^admin/insert-price/form/(?P<pk>.*)', 'form', name="admin-insert-price-form"),
    url(r'^admin/insert-price/form', 'form', name="admin-insert-price-form"),
    url(r'^admin/insert-price/details/(?P<pk>.*)', 'details', name="admin-insert-price-details"),
    url(r'^admin/insert-price/delete/(?P<pk>.*)', 'delete', name="admin-insert-price-delete"),
    url(r'^admin/insert-price/list', 'list', name="admin-insert-price-list"),
    url(r'^admin/insert-price', 'index', name="admin-insert-price-index"),
)