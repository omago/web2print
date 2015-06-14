#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('finish_price.backend_views',
    url(r'^admin/finish-price/form/(?P<pk>.*)', 'form', name="admin-finish-price-form"),
    url(r'^admin/finish-price/form', 'form', name="admin-finish-price-form"),
    url(r'^admin/finish-price/details/(?P<pk>.*)', 'details', name="admin-finish-price-details"),
    url(r'^admin/finish-price/delete/(?P<pk>.*)', 'delete', name="admin-finish-price-delete"),
    url(r'^admin/finish-price/list', 'list', name="admin-finish-price-list"),
    url(r'^admin/finish-price', 'index', name="admin-finish-price-index"),
)