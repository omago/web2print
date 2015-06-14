#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('finish_type.backend_views',
    url(r'^admin/finish-type/form/(?P<pk>.*)', 'form', name="admin-finish-type-form"),
    url(r'^admin/finish-type/form', 'form', name="admin-finish-type-form"),
    url(r'^admin/finish-type/get-type-for-finish', 'get_type_for_finish', name="admin-finish-type-get-type-for-finish"),
    url(r'^admin/finish-type/get-selected-finish-types-for-product', 'get_selected_finish_types_for_product', name="admin-finish-type-get-selected-finish-types-for-product"),
    url(r'^admin/finish-type/details/(?P<pk>.*)', 'details', name="admin-finish-type-details"),
    url(r'^admin/finish-type/delete/(?P<pk>.*)', 'delete', name="admin-finish-type-delete"),
    url(r'^admin/finish-type/list', 'list', name="admin-finish-type-list"),
    url(r'^admin/finish-type', 'index', name="admin-finish-type-index"),
)