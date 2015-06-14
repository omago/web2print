#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from django.core import serializers
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf

from .models import FinishType
from .forms import FinishTypeForm, FinishTypeSearchForm

context = {'page_title': "Tipovi dorada"}

@login_required()
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def index(request):
    return HttpResponseRedirect(reverse("admin-finish-type-list"))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def list(request):
    order_by = request.GET.get("order_by")
    order_type = request.GET.get("order_type")
    finish = request.GET.get("finish", None)

    rows_list = FinishType.objects.all()\
        .annotate(number_of_prices=Count('finishprice', distinct=True))

    if finish:
        rows_list = rows_list.filter(finish_id=finish)

    initial_data = {"finish": finish}
    search_form = FinishTypeSearchForm(initial=initial_data)

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
    context["finish"] = finish
    context["form_url"] = create_url("admin-finish-price-form", request)

    return render_to_response('backend/finish_type/list.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def get_type_for_finish(request):
    finish = request.GET.get("finish")
    finish_types = FinishType.objects.filter(finish=finish)

    data = serializers.serialize("json", finish_types)

    return HttpResponse(data, content_type='application/json')

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def get_selected_finish_types_for_product(request):
    product = request.GET.get("product")
    finish_types = FinishType.objects.filter(product=product)
    data = serializers.serialize("json", finish_types)

    return HttpResponse(data, content_type='application/json')


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def form(request, pk=None):
    finish = request.GET.get("finish", None)

    if request.POST:
        if pk:
            object = FinishType.objects.get(pk=pk)
            form = FinishTypeForm(request.POST, instance=object)
        else:
            form = FinishTypeForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(create_url("admin-finish-price-list", request))
    else:
        if pk:
            object = FinishType.objects.get(pk=pk)
            form = FinishTypeForm(instance=object)
        else:
            form = FinishTypeForm(initial={"finish": finish})


    context.update(csrf(request))

    context['form'] = form
    context["back_url"] = create_url("admin-finish-price-list", request)

    return render_to_response('backend/finish_type/form.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def details(request, pk):
    row = FinishType.objects.get(pk=pk)
    context['row'] = row

    return render_to_response('backend/finish_type/details.html', context, context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-login"))
def delete(request, pk):
    entry = FinishType.objects.get(pk=pk)
    entry.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_url(url, request):
    finish = request.GET.get("finish", None)

    query_string = []

    if finish:
        query_string.append("finish=" + finish)

    return_url = reverse(url)

    if query_string:
        return_url += "?" + "&".join(query_string)

    return return_url