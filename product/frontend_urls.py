#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('product.frontend_views',
    url(r'^(?P<category>[a-zA-Z0-9_-]+)/(?P<subcategory>[a-zA-Z0-9_-]+)/(?P<product>[a-zA-Z0-9_-]+)', 'view', name="product-view"),
    url(r'^product/calculate-price', 'calculate_price', name="product-calculate-price"),
)