#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from product_category.models import ProductCategory
from product_subcategory.models import ProductSubcategory
from cart_product.forms import CartProductForm
from .models import Product

from cart_product.price_calculation import PriceCalculation

def calculate_price(request):

    if request.is_ajax():
        price_calculation = PriceCalculation(
            product=request.POST.get("product", None),
            paper_format=request.POST.get("format_choices", None),
            paper=request.POST.get("paper", None),
            press=request.POST.get("press", None),
            number_of_copies=request.POST.get("number_of_copies", None),
            has_insert=request.POST.get("has_insert", None),
            number_of_inserts=request.POST.get("number_of_inserts", None),
            insert_print=request.POST.get("insert_print", None),
            insert_paper=request.POST.get("insert_paper", None),
            insert_press=request.POST.get("insert_press", None),
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

