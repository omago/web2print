#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('product.backend_views',
    url(r'^admin/product/form/(?P<pk>.*)', 'form', name="admin-product-form"),
    url(r'^admin/product/form', 'form', name="admin-product-form"),
    url(r'^admin/product/is-finish-on-for-product', 'is_finish_on_for_product', name="admin-product-is-finish-on-for-product"),
    url(r'^admin/product/get-selected-finish-types-for-product', 'get_selected_finish_types_for_product', name="admin-finish-type-get-selected-finish-types-for-product"),
    url(r'^admin/product/details/(?P<pk>.*)', 'details', name="admin-product-details"),
    url(r'^admin/product/delete/(?P<pk>.*)', 'delete', name="admin-product-delete"),
    url(r'^admin/product/list/(?P<subcategory>.*)', 'list', name="admin-product-list"),
    url(r'^admin/product/list', 'list', name="admin-product-list"),
    url(r'^admin/product', 'index', name="admin-product-index"),
)