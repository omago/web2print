#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from banner.models import Banner

def index(request):
    context = {}
    try:
        context["bottom_large_banner"] = Banner.objects.filter(banner_position_id=1).order_by('?')[0]
    except IndexError:
        pass

    try:
        context["bottom_left_small_banner"] = Banner.objects.filter(banner_position_id=2).order_by('?')[0]
    except IndexError:
        pass

    try:
        context["bottom_right_small_banner"] = Banner.objects.filter(banner_position_id=3).order_by('?')[0]
    except IndexError:
        pass

    return render_to_response("frontend/frontpage/index.html", context, context_instance=RequestContext(request))