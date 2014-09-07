#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import ProductSubcategory


class ProductSubcategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductSubcategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ProductSubcategory
        exclude = ["slug"]