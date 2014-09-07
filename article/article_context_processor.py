#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import Article
from article_category.models import ArticleCategory

def informations(request):
    information_category = ArticleCategory.objects.get(slug="informacije")
    return {"information_category": information_category,
            "information_category_articles": Article.objects.all().filter(article_category=information_category).order_by("pk") }