#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('product_category.backend_views',
    url(r'^admin/product-category/form/(?P<pk>.*)', 'form', name="admin-product-category-form"),
    url(r'^admin/product-category/form', 'form', name="admin-product-category-form"),
    url(r'^admin/product-category/details/(?P<pk>.*)', 'details', name="admin-product-category-details"),
    url(r'^admin/product-category/delete/(?P<pk>.*)', 'delete', name="admin-product-category-delete"),
    url(r'^admin/product-category/list', 'list', name="admin-product-category-list"),
    url(r'^admin/product-category', 'index', name="admin-product-category-index"),
)