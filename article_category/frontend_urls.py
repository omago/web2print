#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('article_category.frontend_views',
    url(r'^(?P<category>[a-zA-Z0-9_-]+)', 'index', name="article-category-list"),
)