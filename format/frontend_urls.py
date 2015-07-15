#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('format.frontend_views',
    url(r'^format/add-format', 'add_format', name="format-add-format"),
)