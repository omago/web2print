#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from .models import ProductCategory

from django.shortcuts import render_to_response

def index(request, category):
    return render_to_response('frontend/frontpage/index.html', {}, context_instance=RequestContext(request))

