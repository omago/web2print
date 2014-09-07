#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from .models import Product
from product_category.models import ProductCategory
from product_subcategory.models import ProductSubcategory

from django.shortcuts import render_to_response

def view(request, category, subcategory, product):
    print category
    return render_to_response('frontend/product/index.html', {}, context_instance=RequestContext(request))

