#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-index"))
def index(request):
    # context = {'page_title': "Početna"}
    # return render_to_response('default/index.html', context, context_instance=RequestContext(request))
    return HttpResponseRedirect(reverse("admin-product-list"))


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy("admin-index"))
def access_denied(request):
    context = {'page_title': "ACCESS DENIED"}
    return render_to_response('default/access_denied.html', context, context_instance=RequestContext(request))
