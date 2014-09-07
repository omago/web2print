#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import ProductCategory


class ProductCategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductCategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ProductCategory
        exclude = ['slug']