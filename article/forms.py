#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'editor'

    class Meta:
        model = Article
        exclude = ['slug']