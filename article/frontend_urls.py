#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('article.frontend_views',
    url(r'^clanak/(?P<category>[a-zA-Z0-9_-]+)/(?P<article>[a-zA-Z0-9_-]+).html', 'view', name="article-view"),
)