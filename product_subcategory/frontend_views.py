#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from .models import ProductSubcategory
from product.models import Product
from product_category.models import ProductCategory
from django.shortcuts import render_to_response

def list(request, category, subcategory):
    category = ProductCategory.objects.filter(slug=category).get()
    subcategory = ProductSubcategory.objects.filter(category=category).filter(slug=subcategory).get()
    products = Product.objects.filter(subcategory=subcategory).order_by("pk")
    context = {"category": category,
               "page_title": subcategory.name,
               "subcategory": subcategory,
               "products": products,
               "meta_keywords": subcategory.meta_keywords,
               "meta_description": subcategory.meta_keywords}

    return render_to_response('frontend/product_subcategory/list.html', context, context_instance=RequestContext(request))

