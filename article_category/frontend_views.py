#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from .models import ArticleCategory

from django.shortcuts import render_to_response

def index(request, category):
    print category
    return render_to_response('frontend/article_category/index.html', {}, context_instance=RequestContext(request))

