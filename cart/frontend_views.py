#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

def cart(request):


    return render_to_response('frontend/cart/cart.html', {}, context_instance=RequestContext(request))

