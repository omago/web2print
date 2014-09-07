#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('cart.frontend_views',
    url(r'^kosarica', 'cart', name="cart")
)