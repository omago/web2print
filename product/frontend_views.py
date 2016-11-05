#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from cart_product.calculators.price_calculation import PriceCalculation
from cart_product.forms import CartProductForm
from product_category.models import ProductCategory
from product_subcategory.models import ProductSubcategory
from .models import Product


def calculate_price(request):

    if request.is_ajax():
        price_calculation = PriceCalculation(
            data=request.POST,
            user=request.user,
        )

        price_calculation.calculate_price()

        response_data = {'product_price': price_calculation.get_price()}

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def view(request, category, subcategory, product):

    category = ProductCategory.objects.get(slug=category)
    subcategory = ProductSubcategory.objects.filter(slug=subcategory).filter(category=category).get()
    product = Product.objects.filter(subcategory=subcategory).filter(slug=product).get()

    initial = {"has_insert_print": True}

    if product.turn_on_cover:
        initial["has_cover"] = True

    if request.POST:
        form = CartProductForm(product=product, user=request.user, request=request, data=request.POST)

        if form.is_valid():
            form.save()

    else:
        form = CartProductForm(product=product, user=request.user, request=request, initial=initial)

    context = {"category": category,
               "subcategory": subcategory,
               "page_title": product.name,
               "product": product,
               "form": form,
               "meta_keywords": product.meta_keywords,
               "meta_description": product.meta_keywords}

    return render_to_response('frontend/product/view.html', context, context_instance=RequestContext(request))

