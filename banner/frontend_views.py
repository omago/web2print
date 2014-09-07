#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from .models import Banner

from django.shortcuts import render_to_response

def index(request, category):
    print category
    return render_to_response('frontend/banner/index.html', {}, context_instance=RequestContext(request))

