#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from .models import Product
from product_category.models import ProductCategory
from product_subcategory.models import ProductSubcategory
from cart_product.forms import CartProductForm

from django.shortcuts import render_to_response

def view(request, category, subcategory, product):

    category = ProductCategory.objects.get(slug=category)
    subcategory = ProductSubcategory.objects.filter(slug=subcategory).filter(category=category).get()
    product = Product.objects.filter(subcategory=subcategory).filter(slug=product).get()
    form = CartProductForm(product=product)

    context = {"category": category,
               "subcategory": subcategory,
               "page_title": product.name,
               "product": product,
               "form": form,
               "meta_keywords": product.meta_keywords,
               "meta_description": product.meta_keywords}

    return render_to_response('frontend/product/view.html', context, context_instance=RequestContext(request))

