#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('article_category.backend_views',
    url(r'^admin/article-category/form/(?P<pk>.*)', 'form', name="admin-article-category-form"),
    url(r'^admin/article-category/form', 'form', name="admin-article-category-form"),
    url(r'^admin/article-category/details/(?P<pk>.*)', 'details', name="admin-article-category-details"),
    url(r'^admin/article-category/delete/(?P<pk>.*)', 'delete', name="admin-article-category-delete"),
    url(r'^admin/article-category/list', 'list', name="admin-article-category-list"),
    url(r'^admin/article-category', 'index', name="admin-article-category-index"),
)