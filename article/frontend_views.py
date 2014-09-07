#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from .models import Article

from django.shortcuts import render_to_response

def view(request, category, article):
    context = {"article": Article.objects.filter(article_category__slug=category).filter(slug=article).get()}
    return render_to_response('frontend/article/view.html', context, context_instance=RequestContext(request))