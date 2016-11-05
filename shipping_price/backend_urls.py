#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('shipping_price.backend_views',
    url(r'^admin/shipping-price/form/(?P<pk>.*)', 'form', name="admin-shipping-price-form"),
    url(r'^admin/shipping-price/form', 'form', name="admin-shipping-price-form"),
    url(r'^admin/shipping-price/details/(?P<pk>.*)', 'details', name="admin-shipping-price-details"),
    url(r'^admin/shipping-price/delete/(?P<pk>.*)', 'delete', name="admin-shipping-price-delete"),
    url(r'^admin/shipping-price/list', 'list', name="admin-shipping-price-list"),
    url(r'^admin/shipping-price', 'index', name="admin-shipping-price-index"),
)