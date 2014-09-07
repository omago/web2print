#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf

from .models import ProductSubcategory
from .forms import ProductSubcategoryForm

context = {'page_title': "Podkategorije proizvoda"}

@login_required()
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def index(request):
    return HttpResponseRedirect(reverse("admin-product-subcategory-list"))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def list(request, category=None):
    order_by = request.GET.get("order_by")
    order_type = request.GET.get("order_type")
    rows_list = ProductSubcategory.objects.all().annotate(number_of_products=Count('product'))

    if category:
        rows_list = rows_list.filter(category_id=category)

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
    return render_to_response('backend/product_subcategory/list.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def form(request, pk=None):
    if request.POST:
        if pk:
            object = ProductSubcategory.objects.get(pk=pk)
            form = ProductSubcategoryForm(request.POST, instance=object)
        else:
            form = ProductSubcategoryForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("admin-product-subcategory-list"))
    else:
        if pk:
            object = ProductSubcategory.objects.get(pk=pk)
            form = ProductSubcategoryForm(instance=object)
        else:
            form = ProductSubcategoryForm()

    context.update(csrf(request))

    context['form'] = form

    return render_to_response('backend/product_subcategory/form.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def details(request, pk):
    context['row'] = ProductSubcategory.objects.get(pk=pk)

    return render_to_response('backend/product_subcategory/details.html', context, context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def delete(request, pk):
    entry = ProductSubcategory.objects.get(pk=pk)
    entry.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))