#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf

from .models import Format
from .forms import FormatForm

context = {'page_title': "Formati proizvoda"}

@login_required()
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def index(request):
    return HttpResponseRedirect(reverse("admin-format-list"))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def list(request):
    order_by = request.GET.get("order_by")
    order_type = request.GET.get("order_type")
    rows_list = Format.objects.all()

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
    return render_to_response('backend/format/list.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def form(request, pk=None):
    if request.POST:
        if pk:
            object = Format.objects.get(pk=pk)
            form = FormatForm(request.POST, instance=object)
        else:
            form = FormatForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("admin-format-list"))
    else:
        if pk:
            object = Format.objects.get(pk=pk)
            form = FormatForm(instance=object)
        else:
            form = FormatForm()

    context.update(csrf(request))

    context['form'] = form

    return render_to_response('backend/format/form.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def details(request, pk):
    row = Format.objects.get(pk=pk)
    context['row'] = row

    return render_to_response('backend/format/details.html', context, context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def delete(request, pk):
    entry = Format.objects.get(pk=pk)
    entry.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
