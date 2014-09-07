#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import ProductCategory

def product_categories(request):
    return {'product_categories': ProductCategory.objects.all().order_by("pk") }