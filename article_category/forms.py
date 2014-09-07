#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import ArticleCategory


class ArticleCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticleCategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ArticleCategory
        exclude = ['slug']