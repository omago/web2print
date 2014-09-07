#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('product_subcategory.backend_views',
    url(r'^admin/product-subcategory/form/(?P<pk>.*)', 'form', name="admin-product-subcategory-form"),
    url(r'^admin/product-subcategory/form', 'form', name="admin-product-subcategory-form"),
    url(r'^admin/product-subcategory/details/(?P<pk>.*)', 'details', name="admin-product-subcategory-details"),
    url(r'^admin/product-subcategory/delete/(?P<pk>.*)', 'delete', name="admin-product-subcategory-delete"),
    url(r'^admin/product-subcategory/list/(?P<category>.*)', 'list', name="admin-product-subcategory-list"),
    url(r'^admin/product-subcategory/list', 'list', name="admin-product-subcategory-list"),
    url(r'^admin/product-subcategory', 'index', name="admin-product-subcategory-index"),
)