#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf

from .models import Product, ProductFinish, ProductCoverFinish
from .forms import ProductForm

context = {'page_title': "Proizvodi"}

@login_required()
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def index(request):
    return HttpResponseRedirect(reverse("admin-product-list"))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def list(request, subcategory=None):
    order_by = request.GET.get("order_by")
    order_type = request.GET.get("order_type")
    rows_list = Product.objects.all()

    if subcategory:
        rows_list = rows_list.filter(subcategory_id=subcategory)

    if order_by:
        if order_type == "asc":
            order = order_by
        else:
            order = "-" + order_by
        rows_list = rows_list.order_by(order)

    paginator = Paginator(rows_list, settings.RESULTS_PER_PAGE)

    page = request.GET.get('page')
    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rows = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rows = paginator.page(paginator.num_pages)

    context["rows"] = rows
    return render_to_response('backend/product/list.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def form(request, pk=None):
    if request.POST:
        if pk:
            object = Product.objects.get(pk=pk)
            form = ProductForm(request.POST, request.FILES, instance=object)
        else:
            form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()
            form.save_m2m()
            product.save_finishes(request)
            product.save_cover_finishes(request)
            product.save_finish_types(request)
            product.save_cover_finish_types(request)

            return HttpResponseRedirect(reverse("admin-product-list"))
    else:
        if pk:
            object = Product.objects.get(pk=pk)
            form = ProductForm(instance=object)
        else:
            form = ProductForm()

    context.update(csrf(request))

    context['form'] = form
    context['product_id'] = pk

    return render_to_response('backend/product/form.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def details(request, pk):
    row = Product.objects.get(pk=pk)
    context['row'] = row

    return render_to_response('backend/product/details.html', context, context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def delete(request, pk):
    entry = Product.objects.get(pk=pk)
    entry.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def is_finish_on_for_product(request):
    product = request.GET.get("product")
    finish = request.GET.get("finish")
    name = request.GET.get("name")
    response = {"is_on": False}

    if name == "finish":
        model = ProductFinish
    elif name == "cover_finish":
        model = ProductCoverFinish

    try:
        product_finish = model.objects.filter(product_id=product).filter(finish_id=finish).get()
        if product_finish.turn_on:
            response["is_on"] = True
    except ProductFinish.DoesNotExist:
        pass

    data = json.dumps(response)

    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def get_selected_finish_types_for_product(request):
    product_id = request.GET.get("product")
    name = request.GET.get("name")
    finish_types = []

    product = Product.objects.get(pk=product_id)

    if name == "finish_type":
        finish_types = product.finish_type.all()
    elif name == "cover_finish_type":
        finish_types = product.cover_finish_type.all()

    data = serializers.serialize("json", finish_types)

    return HttpResponse(data, content_type='application/json')