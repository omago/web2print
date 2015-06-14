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

from .models import FinishPrice
from .forms import FinishPriceForm, FinishPriceSearchForm

context = {'page_title': "Cijene dorada"}

@login_required()
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def index(request):
    return HttpResponseRedirect(reverse("admin-finish-price-list"))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def list(request):
    order_by = request.GET.get("order_by")
    order_type = request.GET.get("order_type")
    finish = request.GET.get("finish", None)
    finish_type = request.GET.get("finish_type", None)
    rows_list = FinishPrice.objects.all()

    if finish:
        rows_list = rows_list.filter(finish_id=finish)
    if finish_type:
        rows_list = rows_list.filter(finish_type_id=finish_type)

    initial_data = {"finish": finish,
                    "finish_type": finish_type}

    search_form = FinishPriceSearchForm(initial=initial_data, finish=finish)

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
    context["search_form"] = search_form
    context["form_url"] = create_url("admin-finish-price-form", request)

    return render_to_response('backend/finish_price/list.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def form(request, pk=None):
    finish = request.GET.get("finish", None)
    finish_type = request.GET.get("finish_type", None)

    if request.POST:
        if pk:
            object = FinishPrice.objects.get(pk=pk)
            form = FinishPriceForm(request.POST, instance=object)
        else:
            form = FinishPriceForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(create_url("admin-finish-price-list", request))

    else:
        if pk:
            object = FinishPrice.objects.get(pk=pk)
            form = FinishPriceForm(instance=object)
        else:
            form = FinishPriceForm(initial={"finish": finish,
                                            "finish_type": finish_type})

    context.update(csrf(request))
    context['form'] = form
    context["back_url"] = create_url("admin-finish-price-list", request)

    return render_to_response('backend/finish_price/form.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def details(request, pk):
    row = FinishPrice.objects.get(pk=pk)
    context['row'] = row

    return render_to_response('backend/finish_price/details.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def delete(request, pk):
    entry = FinishPrice.objects.get(pk=pk)
    entry.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_url(url, request):
    finish = request.GET.get("finish", None)
    finish_type = request.GET.get("finish_type", None)

    query_string = []

    if finish:
        query_string.append("finish=" + finish)
    if finish_type:
        query_string.append("finish_type=" + finish_type)

    return_url = reverse(url)

    if query_string:
        return_url += "?" + "&".join(query_string)

    return return_url