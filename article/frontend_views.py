#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from .models import Article

from django.shortcuts import render_to_response

def view(request, category, article):
    article = Article.objects.filter(article_category__slug=category).filter(slug=article).get()

    context = {"article": article,
               "page_title": article.name,
               "meta_keywords": article.meta_keywords,
               "meta_description": article.meta_keywords}
    return render_to_response('frontend/article/view.html', context, context_instance=RequestContext(request))