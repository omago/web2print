#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('article.backend_views',
    url(r'^admin/article/form/(?P<pk>.*)', 'form', name="admin-article-form"),
    url(r'^admin/article/form', 'form', name="admin-article-form"),
    url(r'^admin/article/details/(?P<pk>.*)', 'details', name="admin-article-details"),
    url(r'^admin/article/delete/(?P<pk>.*)', 'delete', name="admin-article-delete"),
    url(r'^admin/article/list/(?P<article_category>.*)', 'list', name="admin-article-list"),
    url(r'^admin/article/list', 'list', name="admin-article-list"),
    url(r'^admin/article', 'index', name="admin-article-index"),
)