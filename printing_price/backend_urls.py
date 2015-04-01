#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('printing_price.backend_views',
    url(r'^admin/printing-price/form/(?P<pk>.*)', 'form', name="admin-printing-price-form"),
    url(r'^admin/printing-price/form', 'form', name="admin-printing-price-form"),
    url(r'^admin/printing-price/details/(?P<pk>.*)', 'details', name="admin-printing-price-details"),
    url(r'^admin/printing-price/delete/(?P<pk>.*)', 'delete', name="admin-printing-price-delete"),
    url(r'^admin/printing-price/list', 'list', name="admin-printing-price-list"),
    url(r'^admin/printing-price', 'index', name="admin-printing-price-index"),
)