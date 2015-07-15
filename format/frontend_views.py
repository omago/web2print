#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from product.models import Product
from .models import Format


@login_required
def add_format(request):
    if request.is_ajax() and not request.user.is_anonymous():
        user_format_width = request.GET.get("user_format_width", None)
        product_id = request.GET.get("product_id", None)
        user_format_height = request.GET.get("user_format_height", None)
        user_format_add_to_my_formats = int(request.GET.get("user_format_add_to_my_formats", None))
        format_type = "new"

        product = Product.objects.get(pk=product_id)

        if user_format_add_to_my_formats == 1:
            user_format_add_to_my_formats = True
        else:
            user_format_add_to_my_formats = False

        try:
            product_format = Format.objects\
                .filter(user__isnull=True)\
                .filter(width=user_format_width)\
                .filter(height=user_format_height)\
                .filter(user_format=False)\
                .get()

        except Format.DoesNotExist:
            product_format = None

        if not product_format or product not in product_format.product_formats.all():
            try:
                product_format = Format.objects\
                    .filter(user=request.user)\
                    .filter(width=user_format_width)\
                    .filter(height=user_format_height)\
                    .filter(product_subcategory=product.subcategory)\
                    .get()

                if user_format_add_to_my_formats is True and product_format.user_format is False:
                    product_format.user_format = True
                    product_format.save()

            except Format.DoesNotExist:
                product_format = Format()

                product_format.user = request.user
                product_format.width = user_format_width
                product_format.height = user_format_height
                product_format.user_format = user_format_add_to_my_formats
                product_format.product_subcategory = product.subcategory

                product_format.save()
        else:
            format_type = "old"

        response_data = {"label": str(product_format), "id": product_format.pk, "format_type": format_type}

        return HttpResponse(json.dumps(response_data), content_type="application/json")