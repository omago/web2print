#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('product_subcategory.frontend_views',
    url(r'^(?P<category>[a-zA-Z0-9_-]+)/(?P<subcategory>[a-zA-Z0-9_-]+)', 'list', name="product-subcategory-list"),
)